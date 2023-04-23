from src.operations.Operation import Operation
from src.Expression import Expression
from src.SplitResult import SplitResult
from src.Utils import charWithDepthsIndexes, splitInIndexes


class OperationSplitter:
    
    def splitExpression(
        self,
        expression: Expression,
        operation: Operation) -> SplitResult:
      separator = operation.symbol
      sentence = expression.sentence

      operationIndexes = charWithDepthsIndexes(sentence, separator, 0)
      
      newExpressions = list(map(
        lambda subSentence: Expression(subSentence),
        splitInIndexes(sentence, operationIndexes)
      ))
      
      return SplitResult(newExpressions, operation)