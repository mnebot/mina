import argparse
import logging
import os
import signal
import socket
import stat
import threading
from pathlib import Path
from typing import Optional

from mina.protocol import MAX_MESSAGE_BYTES, process_request

DEFAULT_SOCKET_PATH = Path("/run/mina/mina.sock")


def _remove_stale_socket(socket_path: Path) -> None:
    if not socket_path.exists():
        return
    if not stat.S_ISSOCK(socket_path.stat().st_mode):
        raise RuntimeError(f"Socket path exists and is not a socket: {socket_path}")

    probe = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        probe.connect(str(socket_path))
    except (ConnectionRefusedError, FileNotFoundError):
        socket_path.unlink()
    else:
        raise RuntimeError(f"Mina service is already listening at {socket_path}")
    finally:
        probe.close()


def serve(
    socket_path: Path = DEFAULT_SOCKET_PATH,
    *,
    stop_event: Optional[threading.Event] = None,
    ready_event: Optional[threading.Event] = None,
) -> None:
    if not hasattr(socket, "AF_UNIX"):
        raise RuntimeError("Unix domain sockets are not supported on this platform")

    socket_path.parent.mkdir(parents=True, exist_ok=True)
    _remove_stale_socket(socket_path)

    listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    listener.bind(str(socket_path))
    os.chmod(socket_path, 0o660)
    listener.listen()
    listener.settimeout(0.2)
    if ready_event is not None:
        ready_event.set()

    try:
        while stop_event is None or not stop_event.is_set():
            try:
                connection, _ = listener.accept()
            except socket.timeout:
                continue
            with connection:
                with connection.makefile("rb") as request_stream:
                    request = request_stream.readline(MAX_MESSAGE_BYTES + 1)
                connection.sendall(process_request(request))
    finally:
        listener.close()
        try:
            socket_path.unlink()
        except FileNotFoundError:
            pass


def main() -> int:
    parser = argparse.ArgumentParser(prog="mina-service")
    parser.add_argument("--socket-path", type=Path, default=DEFAULT_SOCKET_PATH)
    arguments = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    stop_event = threading.Event()
    signal.signal(signal.SIGTERM, lambda *_: stop_event.set())
    signal.signal(signal.SIGINT, lambda *_: stop_event.set())
    try:
        serve(arguments.socket_path, stop_event=stop_event)
    except OSError as error:
        parser.exit(1, f"mina-service: {error}\n")
    except RuntimeError as error:
        parser.exit(1, f"mina-service: {error}\n")
    return 0
