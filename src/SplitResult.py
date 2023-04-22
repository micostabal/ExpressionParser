from typing import List
from src.operations.Operation import Operation
from src.Expression import Expression

class SplitResult:
    
    def __init__(self,
          expressions: List[Expression],
          operation: Operation
        ) -> None:
      self.expressions = expressions
      self.operation = operation
    
    def isSingleExpression(self):
        return len(self.expressions)==1