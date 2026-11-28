#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
    printf 'Run this installer as root.\n' >&2
    exit 1
fi

cli_user="${1:-}"
if [[ -z "${cli_user}" ]] || ! id "${cli_user}" >/dev/null 2>&1; then
    printf 'Usage: %s <existing-cli-user>\n' "$0" >&2
    exit 2
fi

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/.." && pwd)"

if ! getent group mina >/dev/null; then
    groupadd --system mina
fi

if ! id mina >/dev/null 2>&1; then
    useradd --system --gid mina --no-create-home --shell /usr/sbin/nologin mina
else
    usermod --gid mina mina
fi

usermod --append --groups mina "${cli_user}"
install -d --owner root --group mina --mode 2750 \
    /opt/mina /opt/mina/versions
install -d --owner mina --group mina --mode 0750 /var/log/mina
install --owner root --group root --mode 0644 \
    "${repo_root}/systemd/mina.service" /etc/systemd/system/mina.service

cli_path=/usr/local/bin/mina
if [[ -e "${cli_path}" && ! -L "${cli_path}" ]]; then
    printf '%s exists and is not a symlink; refusing to replace it.\n' "${cli_path}" >&2
    exit 1
fi
if [[ -L "${cli_path}" ]] && [[ "$(readlink "${cli_path}")" != "/opt/mina/current/bin/mina" ]]; then
    printf '%s points elsewhere; refusing to replace it.\n' "${cli_path}" >&2
    exit 1
fi
ln -sfn /opt/mina/current/bin/mina "${cli_path}"

systemctl daemon-reload
systemctl enable mina.service
printf 'Mina service installed. Log out and back in for the %s group membership to apply.\n' "${cli_user}"
