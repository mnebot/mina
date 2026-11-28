from mina.ports import TextInputPort, TextOutputPort


class Core(TextInputPort):
    def __init__(self, output: TextOutputPort) -> None:
        self._output = output

    def submit(self, request: str) -> None:
        self._output.send(f"He rebut: {request}")
