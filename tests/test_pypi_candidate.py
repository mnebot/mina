import hashlib
from io import BytesIO
import json
from urllib.error import HTTPError

import pytest

from scripts.check_pypi_candidate import (
    candidate_upload_required,
    published_candidate_sha256,
)


def test_missing_pypi_candidate_requires_upload(monkeypatch, tmp_path) -> None:
    wheel = tmp_path / "mina_voice_assistant-0.2.0.dev1-py3-none-any.whl"
    wheel.write_bytes(b"wheel")

    def missing_candidate(*args, **_kwargs):
        assert _kwargs["timeout"] == 15
        raise HTTPError(args[0], 404, "Not Found", None, None)

    monkeypatch.setattr("scripts.check_pypi_candidate.urlopen", missing_candidate)

    assert candidate_upload_required("0.2.0.dev1", wheel) is True


def test_identical_published_candidate_is_not_uploaded_again(monkeypatch, tmp_path) -> None:
    wheel = tmp_path / "mina_voice_assistant-0.2.0.dev1-py3-none-any.whl"
    wheel.write_bytes(b"wheel")
    digest = hashlib.sha256(b"wheel").hexdigest()
    response = BytesIO(
        json.dumps(
            {
                "urls": [
                    {
                        "filename": wheel.name,
                        "digests": {"sha256": digest},
                    }
                ]
            }
        ).encode()
    )
    def published_candidate(url, *, timeout):
        assert url.startswith("https://pypi.org/")
        assert timeout == 15
        return response

    monkeypatch.setattr("scripts.check_pypi_candidate.urlopen", published_candidate)

    assert candidate_upload_required("0.2.0.dev1", wheel) is False


def test_different_published_candidate_content_fails(monkeypatch, tmp_path) -> None:
    wheel = tmp_path / "mina_voice_assistant-0.2.0.dev1-py3-none-any.whl"
    wheel.write_bytes(b"new wheel")
    response = BytesIO(
        json.dumps(
            {
                "urls": [
                    {
                        "filename": wheel.name,
                        "digests": {"sha256": "a" * 64},
                    }
                ]
            }
        ).encode()
    )
    def published_candidate(url, *, timeout):
        assert url.startswith("https://pypi.org/")
        assert timeout == 15
        return response

    monkeypatch.setattr("scripts.check_pypi_candidate.urlopen", published_candidate)

    with pytest.raises(ValueError, match="different content"):
        candidate_upload_required("0.2.0.dev1", wheel)


def test_published_candidate_must_contain_expected_wheel(monkeypatch) -> None:
    response = BytesIO(json.dumps({"urls": []}).encode())
    def published_candidate(url, *, timeout):
        assert url.startswith("https://pypi.org/")
        assert timeout == 15
        return response

    monkeypatch.setattr("scripts.check_pypi_candidate.urlopen", published_candidate)

    with pytest.raises(ValueError, match="does not contain"):
        published_candidate_sha256("0.2.0.dev1", "expected.whl")


def test_invalid_pypi_metadata_fails_explicitly(monkeypatch) -> None:
    response = BytesIO(json.dumps({"urls": None}).encode())

    def published_candidate(url, *, timeout):
        assert url.startswith("https://pypi.org/")
        assert timeout == 15
        return response

    monkeypatch.setattr("scripts.check_pypi_candidate.urlopen", published_candidate)

    with pytest.raises(ValueError, match="invalid metadata"):
        published_candidate_sha256("0.2.0.dev1", "expected.whl")
