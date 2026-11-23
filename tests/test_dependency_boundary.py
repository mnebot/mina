import os
import subprocess
import sys
from pathlib import Path


def test_core_imports_without_site_packages() -> None:
    project_root = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(project_root / "src")

    subprocess.run(
        [
            sys.executable,
            "-S",
            "-c",
            "from mina import Core, TextInputPort, TextOutputPort",
        ],
        check=True,
        cwd=project_root,
        env=env,
    )
