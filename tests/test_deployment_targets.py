import json

import pytest

from scripts.deployment_targets import DeploymentTarget, parse_inventory, write_inventory


def test_empty_inventory_is_rejected() -> None:
    with pytest.raises(ValueError, match="empty"):
        parse_inventory(" ")

    with pytest.raises(ValueError, match="at least one"):
        parse_inventory('{"devices":[]}')


def test_malformed_or_unsafe_inventory_is_rejected() -> None:
    with pytest.raises(ValueError, match="valid JSON"):
        parse_inventory("{invalid")

    with pytest.raises(ValueError, match="safe identifier"):
        parse_inventory(
            '{"devices":[{"alias":"pi;touch","host":"pi-a.tailnet.ts.net",'
            '"user":"mina-deploy"}]}'
        )


def test_valid_inventory_parses_and_writes_private_json(tmp_path) -> None:
    raw = json.dumps(
        {
            "devices": [
                {
                    "alias": "kitchen-pi",
                    "host": "mina-kitchen.tailnet.example.ts.net",
                    "user": "mina-deploy",
                },
                {"alias": "garage-pi", "host": "100.64.0.12", "user": "mina-deploy"},
            ]
        }
    )

    targets = parse_inventory(raw)
    output = tmp_path / "private" / "targets.json"
    write_inventory(output, targets)

    assert targets == [
        DeploymentTarget("kitchen-pi", "mina-kitchen.tailnet.example.ts.net", "mina-deploy"),
        DeploymentTarget("garage-pi", "100.64.0.12", "mina-deploy"),
    ]
    assert json.loads(output.read_text(encoding="utf-8"))["devices"][0]["alias"] == "kitchen-pi"


def test_duplicate_aliases_and_root_users_are_rejected() -> None:
    with pytest.raises(ValueError, match="unique"):
        parse_inventory(
            '{"devices":['
            '{"alias":"pi-a","host":"pi-a.tailnet.ts.net","user":"mina-deploy"},'
            '{"alias":"pi-a","host":"pi-b.tailnet.ts.net","user":"mina-deploy"}'
            ']}'
        )

    with pytest.raises(ValueError, match="non-root"):
        parse_inventory(
            '{"devices":[{"alias":"pi-a","host":"pi-a.tailnet.ts.net","user":"root"}]}'
        )
