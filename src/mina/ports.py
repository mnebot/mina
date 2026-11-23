from typing import Protocol


class TextInputPort(Protocol):
    def submit(self, request: str) -> None:
        """Submit a text request to the core."""


class TextOutputPort(Protocol):
    def send(self, response: str) -> None:
        """Deliver a text response from the core."""
