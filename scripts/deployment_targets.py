import argparse
from dataclasses import asdict, dataclass
import ipaddress
import json
import os
from pathlib import Path
import re


_ALIAS = re.compile(r"^[a-z0-9][a-z0-9_-]{0,62}$")
_HOSTNAME = re.compile(
    r"^(?=.{1,253}$)[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*\.?$"
)
_USERNAME = re.compile(r"^[a-z_][a-z0-9_-]{0,31}$")


@dataclass(frozen=True)
class DeploymentTarget:
    alias: str
    host: str
    user: str

    @property
    def ssh_destination(self) -> str:
        try:
            is_ipv6 = ipaddress.ip_address(self.host).version == 6
        except ValueError:
            is_ipv6 = False
        host = f"[{self.host}]" if is_ipv6 else self.host
        return f"{self.user}@{host}"


def _valid_host(host: object) -> bool:
    if not isinstance(host, str) or not host:
        return False
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return _HOSTNAME.fullmatch(host) is not None
    return True


def parse_inventory(raw: str) -> list[DeploymentTarget]:
    if not raw.strip():
        raise ValueError("target inventory is empty")
    try:
        inventory = json.loads(raw)
    except json.JSONDecodeError as error:
        raise ValueError("target inventory is not valid JSON") from error

    if not isinstance(inventory, dict) or set(inventory) != {"devices"}:
        raise ValueError("target inventory must contain only a devices list")
    devices = inventory["devices"]
    if not isinstance(devices, list) or not devices:
        raise ValueError("devices must contain at least one target")

    targets = []
    aliases = set()
    for device in devices:
        if not isinstance(device, dict) or set(device) != {"alias", "host", "user"}:
            raise ValueError("each target must contain alias, host, and user")
        alias = device["alias"]
        host = device["host"]
        user = device["user"]
        if not isinstance(alias, str) or _ALIAS.fullmatch(alias) is None:
            raise ValueError("target alias must be a lowercase safe identifier")
        if alias in aliases:
            raise ValueError("target aliases must be unique")
        if not _valid_host(host):
            raise ValueError("target host must be a hostname or IP address")
        if (
            not isinstance(user, str)
            or user == "root"
            or _USERNAME.fullmatch(user) is None
        ):
            raise ValueError("target user must be a non-root Linux account name")
        aliases.add(alias)
        targets.append(DeploymentTarget(alias=alias, host=host, user=user))
    return targets


def write_inventory(path: Path, targets: list[DeploymentTarget]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    file_descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(file_descriptor, "w", encoding="utf-8") as stream:
        json.dump({"devices": [asdict(target) for target in targets]}, stream)
        stream.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()

    raw_inventory = os.environ.get("MINA_TARGETS_JSON")
    if raw_inventory is None:
        parser.error("MINA_TARGETS_JSON is required")
    try:
        targets = parse_inventory(raw_inventory)
        write_inventory(arguments.output, targets)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    aliases = ", ".join(target.alias for target in targets)
    print(f"Validated {len(targets)} deployment targets: {aliases}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
