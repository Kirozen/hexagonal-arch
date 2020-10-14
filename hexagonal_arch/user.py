from hexagonal_arch.input_port import InputPort


class User:
    def __init__(self, input: InputPort) -> None:
        print("User: __init__")
        self.input = input

    def action(self):
        print("User: action")
        self.input.push("12345")
