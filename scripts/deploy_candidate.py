import argparse
from pathlib import Path
import re
import subprocess

from scripts.deployment_targets import DeploymentTarget, parse_inventory

_CANDIDATE_VERSION = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+\.dev[0-9]+$")

def _run(command: list[str]) -> None:
    subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


def deploy_target(target: DeploymentTarget, version: str) -> None:
    if _CANDIDATE_VERSION.fullmatch(version) is None:
        raise ValueError("version must be a candidate prerelease")
    _run(
        [
            "tailscale",
            "ssh",
            target.ssh_destination,
            "sudo",
            "-n",
            "/usr/local/sbin/mina-deploy-candidate",
            version,
            target.user,
        ]
    )


def deploy_inventory(
    targets: list[DeploymentTarget],
    version: str,
    diagnostics_file: Path,
) -> bool:
    results = []
    for target in targets:
        try:
            deploy_target(target, version)
        except (OSError, subprocess.CalledProcessError, ValueError):
            results.append(
                f"{target.alias}: failed; inspect /var/log/mina/deploy.log on the device"
            )
            print(f"[{target.alias}] deployment failed; on-device log: /var/log/mina/deploy.log")
        else:
            results.append(f"{target.alias}: passed candidate {version}")
            print(f"[{target.alias}] candidate {version} passed")

    diagnostics_file.write_text("\n".join(results) + "\n", encoding="utf-8")
    return all(": passed " in result for result in results)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--diagnostics-file", type=Path, required=True)
    arguments = parser.parse_args()

    try:
        targets = parse_inventory(arguments.inventory.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        parser.error(str(error))

    success = deploy_inventory(
        targets,
        arguments.version,
        arguments.diagnostics_file,
    )
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
