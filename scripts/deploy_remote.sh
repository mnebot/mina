#!/usr/bin/env bash
set -Eeuo pipefail

version="${1:-}"
cli_user="${2:-}"
if [[ "${EUID}" -ne 0 ]]; then
    printf 'Run remote deployment as root.\n' >&2
    exit 1
fi
if [[ ! "${version}" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.dev[0-9]+$ ]]; then
    printf 'Invalid candidate version.\n' >&2
    exit 2
fi
if [[ ! "${cli_user}" =~ ^[a-z_][a-z0-9_-]{0,31}$ ]] || [[ "${cli_user}" == root ]]; then
    printf 'Invalid deployment account.\n' >&2
    exit 2
fi

umask 077
install -d --owner root --group root --mode 0750 /var/log/mina
exec >>/var/log/mina/deploy.log 2>&1
printf 'Starting Mina candidate deployment: %s\n' "${version}"

deployment_root="/usr/local/lib/mina-deploy"
if [[ ! -x "${deployment_root}/scripts/install_systemd_service.sh" ||
    ! -f "${deployment_root}/systemd/mina.service" ]]; then
    printf 'Mina deployment bootstrap files are missing.\n'
    exit 1
fi

if systemctl cat mina.service >/dev/null 2>&1; then
    printf 'Existing Mina service found; ensuring its configuration is installed.\n'
else
    printf 'Mina service is missing; creating it for the first deployment.\n'
fi
"${deployment_root}/scripts/install_systemd_service.sh" "${cli_user}"
umask 027

candidate_path="/opt/mina/versions/${version}"
if ! id mina >/dev/null 2>&1; then
    printf 'Mina service account is missing; refusing deployment.\n'
    exit 1
fi

old_target=""
if [[ -L /opt/mina/current ]]; then
    old_target="$(readlink -f -- /opt/mina/current)"
    if [[ ! -d "${old_target}" || "${old_target}" != /opt/mina/versions/* ]]; then
        printf 'Current Mina environment is invalid; refusing deployment.\n'
        exit 1
    fi
elif [[ -e /opt/mina/current ]]; then
    printf '/opt/mina/current is not a symbolic link; refusing deployment.\n'
    exit 1
fi

switch_current() {
    local target="$1"
    local next_link="/opt/mina/current.next.$$"
    rm -f -- "${next_link}"
    ln -s -- "${target}" "${next_link}"
    mv -Tf -- "${next_link}" /opt/mina/current
}

rollback() {
    local exit_status="$?"
    trap - ERR
    set +e
    if [[ -n "${old_target}" ]]; then
        printf 'Candidate deployment failed; restoring previous environment.\n'
        if switch_current "${old_target}" &&
            systemctl restart mina.service &&
            systemctl is-active --quiet mina.service; then
            printf 'Rollback succeeded.\n'
        else
            printf 'Rollback failed; inspect this device journal and /var/log/mina/deploy.log.\n'
            exit_status=1
        fi
    else
        if ! rm -f -- /opt/mina/current; then
            printf 'Could not remove the failed first-install pointer.\n'
            exit_status=1
        fi
        if ! systemctl stop mina.service; then
            printf 'Could not stop the failed first-install service.\n'
            exit_status=1
        fi
        printf 'First installation failed; no previous environment was available to restore.\n'
    fi
    exit "${exit_status}"
}
trap rollback ERR

systemctl stop mina.service
if [[ "${old_target}" == "${candidate_path}" ]]; then
    systemctl restart mina.service
else
    rm -rf -- "${candidate_path}"
    python3 -m venv "${candidate_path}"
    "${candidate_path}/bin/python" -m pip install \
        --disable-pip-version-check \
        --no-cache-dir \
        --pre \
        --index-url https://pypi.org/simple \
        "mina-voice-assistant==${version}"
    switch_current "${candidate_path}"
    systemctl restart mina.service
fi

installed_version="$(
    /opt/mina/current/bin/python -c \
        'import importlib.metadata; print(importlib.metadata.version("mina-voice-assistant"))'
)"
if [[ "${installed_version}" != "${version}" ]]; then
    printf 'Installed package version did not match the candidate.\n'
    false
fi

ready=false
for _ in $(seq 1 30); do
    if systemctl is-active --quiet mina.service && [[ -S /run/mina/mina.sock ]]; then
        ready=true
        break
    fi
    sleep 1
done
if [[ "${ready}" != true ]]; then
    printf 'Mina service did not become ready.\n'
    false
fi

response="$(runuser -u mina -- /usr/local/bin/mina 'encén el llum')"
if [[ "${response}" != 'He rebut: encén el llum' ]]; then
    printf 'Mina text-response smoke check failed.\n'
    false
fi

trap - ERR
printf 'Candidate deployment and smoke checks succeeded: %s\n' "${version}"
