from abc import ABC, abstractmethod


class OutputPort(ABC):
    def __init__(self) -> None:
        super().__init__()
        print("OutputPort: __init__")

    @abstractmethod
    def write(self, value: str):
        pass
