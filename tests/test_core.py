from mina import Core


class RecordingOutput:
    def __init__(self) -> None:
        self.responses: list[str] = []

    def send(self, response: str) -> None:
        self.responses.append(response)


def test_core_sends_catalan_acknowledgement_to_output_port() -> None:
    output = RecordingOutput()
    core = Core(output)

    core.submit("encén el llum")

    assert output.responses == ["He rebut: encén el llum"]
