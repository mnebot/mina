import argparse
import os
import re
import tomllib
from pathlib import Path

from packaging.version import InvalidVersion, Version


def candidate_version(stable_version: str, run_number: int) -> str:
    if run_number < 1:
        raise ValueError("run_number must be a positive integer")

    try:
        version = Version(stable_version)
    except InvalidVersion as error:
        raise ValueError(f"Invalid stable version: {stable_version}") from error

    if version.is_prerelease or version.is_devrelease or version.local is not None:
        raise ValueError("stable_version must be a stable public version")

    return str(Version(f"{version.public}.dev{run_number}"))


def should_upload_candidate(published_sha256: str | None, built_sha256: str) -> bool:
    if len(built_sha256) != 64 or any(
        character not in "0123456789abcdef" for character in built_sha256.lower()
    ):
        raise ValueError("built_sha256 must be a SHA-256 hex digest")

    if published_sha256 is None:
        return True

    if len(published_sha256) != 64 or any(
        character not in "0123456789abcdef" for character in published_sha256.lower()
    ):
        raise ValueError("published_sha256 must be a SHA-256 hex digest")

    if published_sha256.lower() != built_sha256.lower():
        raise ValueError("candidate version already exists with different content")
    return False


def project_version(project_file: Path) -> str:
    with project_file.open("rb") as stream:
        project = tomllib.load(stream)
    version = project["project"]["version"]
    if not isinstance(version, str):
        raise ValueError("project.version must be a string")
    return version


def set_project_version(project_file: Path, version: str) -> None:
    try:
        normalized_version = str(Version(version))
    except InvalidVersion as error:
        raise ValueError(f"Invalid project version: {version}") from error

    text = project_file.read_text(encoding="utf-8")
    in_project_section = False
    version_line = re.compile(r'^(?P<prefix>\s*version\s*=\s*)"[^"]+"(?P<suffix>\s*)$')
    matches = []
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        stripped_line = line.strip()
        if stripped_line.startswith("["):
            in_project_section = stripped_line == "[project]"
        elif in_project_section and version_line.match(line.rstrip("\r\n")):
            matches.append(index)

    if len(matches) != 1:
        raise ValueError("pyproject.toml must contain one static project.version")

    index = matches[0]
    match = version_line.match(lines[index].rstrip("\r\n"))
    assert match is not None
    newline = "\r\n" if lines[index].endswith("\r\n") else "\n" if lines[index].endswith("\n") else ""
    lines[index] = f'{match.group("prefix")}"{normalized_version}"{match.group("suffix")}{newline}'
    project_file.write_text("".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-file", type=Path, default=Path("pyproject.toml"))
    parser.add_argument("--write-project-version", action="store_true")
    parser.add_argument(
        "--run-number",
        type=int,
        default=os.environ.get("GITHUB_RUN_NUMBER"),
    )
    arguments = parser.parse_args()
    if arguments.run_number is None:
        parser.error("--run-number or GITHUB_RUN_NUMBER is required")

    try:
        base_version = project_version(arguments.project_file)
        candidate = candidate_version(base_version, arguments.run_number)
        if arguments.write_project_version:
            set_project_version(arguments.project_file, candidate)
    except (OSError, KeyError, TypeError, ValueError) as error:
        parser.error(str(error))

    print(candidate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
