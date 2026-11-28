import argparse
import hashlib
import json
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlopen

from scripts.candidate_version import should_upload_candidate


def published_candidate_sha256(version: str, filename: str) -> str | None:
    url = f"https://pypi.org/pypi/mina-voice-assistant/{quote(version, safe='')}/json"
    try:
        with urlopen(url, timeout=15) as response:
            package_data = json.load(response)
    except HTTPError as error:
        if error.code == 404:
            return None
        raise

    urls = package_data.get("urls") if isinstance(package_data, dict) else None
    if not isinstance(urls, list):
        raise ValueError(f"PyPI returned invalid metadata for candidate {version}")
    matching_files = [
        item
        for item in urls
        if isinstance(item, dict) and item.get("filename") == filename
    ]
    if len(matching_files) != 1:
        raise ValueError(
            f"Published candidate {version} does not contain exactly one {filename}"
        )

    digests = matching_files[0].get("digests")
    digest = digests.get("sha256") if isinstance(digests, dict) else None
    if not isinstance(digest, str):
        raise ValueError(f"Published candidate {version} has no SHA-256 digest")
    return digest


def candidate_upload_required(version: str, wheel: Path) -> bool:
    built_sha256 = hashlib.sha256(wheel.read_bytes()).hexdigest()
    published_sha256 = published_candidate_sha256(version, wheel.name)
    return should_upload_candidate(published_sha256, built_sha256)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--wheel", type=Path, required=True)
    parser.add_argument("--github-output", type=Path)
    arguments = parser.parse_args()

    try:
        upload_required = candidate_upload_required(arguments.version, arguments.wheel)
    except (HTTPError, OSError, ValueError) as error:
        parser.error(str(error))

    output = f"upload={'true' if upload_required else 'false'}"
    if arguments.github_output is not None:
        with arguments.github_output.open("a", encoding="utf-8") as stream:
            stream.write(output + "\n")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
