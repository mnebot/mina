import subprocess

import pytest

from scripts.deploy_candidate import deploy_inventory, deploy_target
from scripts.deployment_targets import DeploymentTarget


def test_target_deployment_uses_tailscale_ssh_and_fixed_helper(monkeypatch) -> None:
    commands = []
    monkeypatch.setattr("scripts.deploy_candidate._run", commands.append)
    target = DeploymentTarget("kitchen-pi", "mina-kitchen.tailnet.ts.net", "mina-deploy")

    deploy_target(target, "0.2.0.dev17")

    assert commands == [
        [
            "tailscale",
            "ssh",
            "mina-deploy@mina-kitchen.tailnet.ts.net",
            "sudo",
            "-n",
            "/usr/local/sbin/mina-deploy-candidate",
            "0.2.0.dev17",
            "mina-deploy",
        ]
    ]


def test_deployment_continues_after_device_failure_and_redacts_hosts(
    monkeypatch, tmp_path
) -> None:
    targets = [
        DeploymentTarget("kitchen-pi", "private-kitchen.tailnet.ts.net", "mina-deploy"),
        DeploymentTarget("garage-pi", "private-garage.tailnet.ts.net", "mina-deploy"),
    ]
    attempted = []

    def deploy(target, _version):
        assert _version == "0.2.0.dev17"
        attempted.append(target.alias)
        if target.alias == "garage-pi":
            raise subprocess.CalledProcessError(
                1,
                [
                    "tailscale",
                    "ssh",
                    "private-garage.tailnet.ts.net",
                    "TOP_SECRET",
                ],
            )

    monkeypatch.setattr("scripts.deploy_candidate.deploy_target", deploy)
    diagnostics = tmp_path / "diagnostics.txt"

    assert (
        deploy_inventory(targets, "0.2.0.dev17", diagnostics)
        is False
    )
    assert attempted == ["kitchen-pi", "garage-pi"]
    content = diagnostics.read_text(encoding="utf-8")
    assert "kitchen-pi: passed candidate 0.2.0.dev17" in content
    assert "garage-pi: failed" in content
    assert "private-kitchen" not in content
    assert "private-garage" not in content
    assert "TOP_SECRET" not in content
    assert "encén el llum" not in content
    assert "/var/log/mina/deploy.log" in content


def test_all_devices_must_pass_for_deployment_success(monkeypatch, tmp_path) -> None:
    targets = [
        DeploymentTarget("kitchen-pi", "private-kitchen.tailnet.ts.net", "mina-deploy"),
        DeploymentTarget("garage-pi", "private-garage.tailnet.ts.net", "mina-deploy"),
    ]
    attempted = []

    def deploy(target, version):
        attempted.append((target.alias, version))

    monkeypatch.setattr(
        "scripts.deploy_candidate.deploy_target",
        deploy,
    )
    diagnostics = tmp_path / "diagnostics.txt"

    assert deploy_inventory(targets, "0.2.0.dev17", diagnostics) is True
    assert attempted == [
        ("kitchen-pi", "0.2.0.dev17"),
        ("garage-pi", "0.2.0.dev17"),
    ]
    content = diagnostics.read_text(encoding="utf-8")
    assert "kitchen-pi: passed candidate 0.2.0.dev17" in content
    assert "garage-pi: passed candidate 0.2.0.dev17" in content
    assert "private-" not in content


def test_deployment_rejects_stable_version_before_connecting(monkeypatch) -> None:
    def fail_if_called(_command):
        assert _command[0] == "tailscale"
        pytest.fail("No Tailscale command should run for an invalid candidate")

    monkeypatch.setattr("scripts.deploy_candidate._run", fail_if_called)

    with pytest.raises(ValueError, match="candidate prerelease"):
        deploy_target(
            DeploymentTarget("kitchen-pi", "pi.tailnet.ts.net", "mina-deploy"),
            "0.2.0",
        )
