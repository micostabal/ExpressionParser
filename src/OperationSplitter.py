from typing import List
from functools import reduce
from src.operations.Operation import Operation
from src.Expression import Expression
from src.SplitResult import SplitResult


def charWithDepthsIndexes(sentence: str, targetChar: str, depth: int) -> List[int]:
  indexes=[]
  currentDepth=0
  for index, char in enumerate(sentence):
    if char=='(':
      currentDepth+=1
    elif char==")":
      currentDepth-=1
    elif char==targetChar and depth==currentDepth:
      indexes.append(index)
  return indexes


class OperationSplitter:
    
    def splitExpression(
        self,
        expression: Expression,
        operation: Operation) -> SplitResult:
      separator = operation.symbol
      sentence = expression.sentence
      
      return SplitResult([], None)