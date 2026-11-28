import json
import logging
from typing import Optional

from mina import Core

MAX_MESSAGE_BYTES = 65536
logger = logging.getLogger(__name__)


class _Response:
    def __init__(self) -> None:
        self.value: Optional[str] = None

    def send(self, response: str) -> None:
        self.value = response


def encode_request(text: str) -> bytes:
    message = json.dumps({"text": text}, ensure_ascii=False).encode("utf-8") + b"\n"
    if len(message) > MAX_MESSAGE_BYTES:
        raise ValueError("Text request is too large")
    return message


def decode_response(message: bytes) -> str:
    try:
        response = json.loads(message.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError("Mina service returned an invalid response") from error

    if not isinstance(response, dict):
        raise RuntimeError("Mina service returned an invalid response")
    if "error" in response:
        raise RuntimeError(str(response["error"]))
    result = response.get("response")
    if not isinstance(result, str):
        raise RuntimeError("Mina service returned an invalid response")
    return result


def process_request(message: bytes) -> bytes:
    if len(message) > MAX_MESSAGE_BYTES or not message.endswith(b"\n"):
        logger.warning("Rejected invalid text request")
        return b'{"error":"Invalid request"}\n'

    try:
        request = json.loads(message.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        logger.warning("Rejected invalid text request")
        return b'{"error":"Invalid request"}\n'

    if not isinstance(request, dict) or not isinstance(request.get("text"), str):
        logger.warning("Rejected invalid text request")
        return b'{"error":"Invalid request"}\n'

    output = _Response()
    Core(output).submit(request["text"])
    logger.info("Processed text request")
    return json.dumps({"response": output.value}, ensure_ascii=False).encode("utf-8") + b"\n"
