from src.operations.Operation import Operation


class Multiplication(Operation):
    
    def __init__(self) -> None:
        super().__init__("*")
    
    def resolve(self, a: int, b: int) -> int:
        return a*b