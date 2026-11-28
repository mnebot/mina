from packaging.version import Version
import pytest

from scripts.candidate_version import (
    candidate_version,
    project_version,
    set_project_version,
    should_upload_candidate,
)


def test_candidate_version_is_valid_and_unique_per_run() -> None:
    first = candidate_version("0.2.0", 17)
    second = candidate_version("0.2.0", 18)

    assert first == "0.2.0.dev17"
    assert Version(first).is_devrelease
    assert second == "0.2.0.dev18"
    assert Version(first) < Version(second)


def test_retry_for_same_run_reuses_the_candidate_version() -> None:
    first_attempt = candidate_version("0.2.0", 17)
    retry = candidate_version("0.2.0", 17)

    assert retry == first_attempt


def test_retry_skips_upload_when_published_artifact_is_identical() -> None:
    digest = "a" * 64

    assert should_upload_candidate(digest, digest) is False


def test_new_candidate_is_ready_for_upload() -> None:
    assert should_upload_candidate(None, "b" * 64) is True


def test_retry_rejects_different_content_for_published_version() -> None:
    with pytest.raises(ValueError, match="different content"):
        should_upload_candidate("a" * 64, "b" * 64)


@pytest.mark.parametrize("run_number", [0, -1])
def test_candidate_version_rejects_non_positive_run_number(run_number: int) -> None:
    with pytest.raises(ValueError, match="positive"):
        candidate_version("0.2.0", run_number)


@pytest.mark.parametrize("stable_version", ["not-a-version", "0.2.0.dev1", "0.2.0+local"])
def test_candidate_version_rejects_invalid_or_unstable_base(
    stable_version: str,
) -> None:
    with pytest.raises(ValueError):
        candidate_version(stable_version, 17)


def test_write_candidate_version_only_changes_project_version(tmp_path) -> None:
    project_file = tmp_path / "pyproject.toml"
    project_file.write_text(
        '[project]\nname = "mina-voice-assistant"\nversion = "0.1.0"\n'
        '[tool.example]\nversion = "keep-this"\n',
        encoding="utf-8",
    )

    set_project_version(project_file, "0.1.0.dev17")

    assert project_version(project_file) == "0.1.0.dev17"
    assert '[tool.example]\nversion = "keep-this"' in project_file.read_text(
        encoding="utf-8"
    )


def test_write_project_version_rejects_invalid_version(tmp_path) -> None:
    project_file = tmp_path / "pyproject.toml"
    project_file.write_text('[project]\nversion = "0.1.0"\n', encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid project version"):
        set_project_version(project_file, "not-a-version")
