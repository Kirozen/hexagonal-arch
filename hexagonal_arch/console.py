from hexagonal_arch.output_port import OutputPort


class Console(OutputPort):
    def __init__(self) -> None:
        super().__init__()
        print("Console: __init__")

    def write(self, value: str):
        print("Console: write")
        print(value)
