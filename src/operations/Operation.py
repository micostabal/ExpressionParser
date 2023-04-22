from abc import ABC, abstractmethod

class Operation(ABC):

  def __init__(self, symbol: str) -> None:
    super().__init__()
    self.symbol=symbol
  
  def resolve(self, a: int, b: int) -> int: pass