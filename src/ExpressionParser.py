from typing import List
from functools import reduce
from src.operations.Operation import Operation
from src.Expression import Expression
from src.OperationSplitter import OperationSplitter
from src.SingleTokenEvaluator import SingleTokenEvaluator

class ExpressionParser:
    
    def __init__(self,
                splitter: OperationSplitter,
                evaluator: SingleTokenEvaluator,
                operations: List[Operation]) -> None:
        self.splitter=splitter
        self.evaluator=evaluator
        self.operations=operations
    
    def evaluate(self, expression: Expression) -> int:
        expression.stripRedundantParenthesis()
        for operation in self.operations:
          splitResult=self.splitter.splitExpression(expression, operation)
          if not splitResult.isSingleExpression():
            exprs = list(map(lambda expr: self.evaluate(expr), splitResult.expressions))
            return reduce(
              lambda x, y: operation.resolve(x, y),
              exprs
            )
        return self.evaluator.resolve(splitResult.expressions[0])
