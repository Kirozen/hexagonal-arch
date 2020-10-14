from abc import ABC, abstractmethod


class InputPort(ABC):
    def __init__(self) -> None:
        super().__init__()
        print("InputPort: __init__")

    @abstractmethod
    def push(self, data: str):
        pass
