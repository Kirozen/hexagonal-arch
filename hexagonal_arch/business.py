from hexagonal_arch.input_port import InputPort
from hexagonal_arch.output_port import OutputPort


class Business(InputPort):
    def __init__(self, output: OutputPort) -> None:
        super().__init__()
        print("Business: __init__")
        self.output = output

    def push(self, data: str):
        print("Business: push")
        self.output.write(f"The data is: {data}")
