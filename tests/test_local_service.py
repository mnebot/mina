import json
import logging
import socket
import sys
import threading
from pathlib import Path

import pytest

from mina import cli
from mina.protocol import decode_response, encode_request, process_request
from mina.service import serve


def test_service_processes_text_through_core() -> None:
    response = process_request(encode_request("encén el llum"))

    assert decode_response(response) == "He rebut: encén el llum"


def test_service_rejects_malformed_requests_without_echoing_them() -> None:
    response = process_request(b'{"text":"private text"')

    assert json.loads(response) == {"error": "Invalid request"}
    assert b"private text" not in response


def test_operational_logs_do_not_include_request_or_response_text(caplog) -> None:
    request_text = "private request"
    caplog.set_level(logging.INFO, logger="mina.protocol")

    process_request(encode_request(request_text))

    assert "Processed text request" in caplog.text
    assert request_text not in caplog.text
    assert f"He rebut: {request_text}" not in caplog.text


def test_cli_reports_unavailable_service(monkeypatch, capsys) -> None:
    class UnavailableSocket:
        def __init__(self, *_args) -> None:
            pass

        def __enter__(self):
            return self

        def __exit__(self, *_args) -> None:
            pass

        def connect(self, _address: str) -> None:
            raise FileNotFoundError("socket is unavailable")

    monkeypatch.setattr(socket, "AF_UNIX", 1, raising=False)
    monkeypatch.setattr(socket, "socket", UnavailableSocket)
    monkeypatch.setattr(sys, "argv", ["mina", "hello"])

    assert cli.main() == 1
    captured = capsys.readouterr()
    assert "socket is unavailable" in captured.err
    assert captured.out == ""


@pytest.mark.skipif(not hasattr(socket, "AF_UNIX"), reason="Unix sockets unavailable")
def test_cli_round_trip_to_resident_service(tmp_path: Path) -> None:
    socket_path = tmp_path / "mina.sock"
    ready_event = threading.Event()
    stop_event = threading.Event()
    server = threading.Thread(
        target=serve,
        args=(socket_path,),
        kwargs={"stop_event": stop_event, "ready_event": ready_event},
        daemon=True,
    )
    server.start()
    try:
        assert ready_event.wait(timeout=2)
        assert cli.send_text("encén el llum", socket_path) == "He rebut: encén el llum"
    finally:
        stop_event.set()
        server.join(timeout=2)
    assert not server.is_alive()
