import argparse
import socket
import sys
from pathlib import Path

from mina.protocol import MAX_MESSAGE_BYTES, decode_response, encode_request
from mina.service import DEFAULT_SOCKET_PATH


def send_text(text: str, socket_path: Path = DEFAULT_SOCKET_PATH) -> str:
    if not hasattr(socket, "AF_UNIX"):
        raise RuntimeError("Unix domain sockets are not supported on this platform")

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as connection:
        connection.connect(str(socket_path))
        connection.sendall(encode_request(text))
        with connection.makefile("rb") as response_stream:
            response = response_stream.readline(MAX_MESSAGE_BYTES + 1024)
    if not response:
        raise RuntimeError("Mina service closed the connection without a response")
    return decode_response(response)


def main() -> int:
    parser = argparse.ArgumentParser(prog="mina")
    parser.add_argument("text", help="Text request to send to Mina")
    parser.add_argument("--socket-path", type=Path, default=DEFAULT_SOCKET_PATH)
    arguments = parser.parse_args()

    try:
        response = send_text(arguments.text, arguments.socket_path)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"mina: {error}", file=sys.stderr)
        return 1

    print(response)
    return 0
