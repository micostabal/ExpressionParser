from typing import Dict
from src.Expression import Expression


class SingleTokenEvaluator:
    
    def __init__(self, vars: Dict[str, int]) -> None:
        self.vars = vars
    
    def addVar(self, name, value):
        vars[name] = value
    
    def resolve(self, expression: Expression):
        token = expression.sentence
        if (token in self.vars):
            return self.vars[token]
        return int(token)