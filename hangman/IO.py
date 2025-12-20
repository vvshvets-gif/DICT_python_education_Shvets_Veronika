from abc import ABC, abstractmethod

class IO(ABC):
    @abstractmethod
    def get_input(self, prompt: str) -> str:
        pass

    @abstractmethod
    def print_output(self, value: str):
        pass

class ConsoleIO(IO):
    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def print_output(self, message: str):
        print(message)