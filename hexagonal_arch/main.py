from hexagonal_arch.business import Business
from hexagonal_arch.console import Console
from hexagonal_arch.input_port import InputPort
from hexagonal_arch.output_port import OutputPort
from hexagonal_arch.user import User


def main():
    console: OutputPort = Console()
    business: InputPort = Business(console)
    user = User(business)

    user.action()


if __name__ == "__main__":
    main()
