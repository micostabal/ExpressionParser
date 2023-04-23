from src.Utils import charWithDepthsIndexes
from src.operations.Operations import OPERATIONS

class Expression:
    
    def __init__(self, sentence) -> None:
        self.sentence=sentence

    def getZeroLevelOperations(self):
        return list(map(
            lambda x: len(charWithDepthsIndexes(self.sentence, x.symbol, 0)),
            OPERATIONS))
    
    def isSurroundedByParenthesis(self):
        return self.sentence[0]=='(' and self.sentence[len(self.sentence)-1]==')'
    
    def hasZeroLevelOperations(self):
        return sum(self.getZeroLevelOperations())==0
    
    def removeOuterParenthesis(self) -> None:
        self.sentence=self.sentence[1:len(self.sentence)-1]

    def stripRedundantParenthesis(self) -> None:
        while (self.hasZeroLevelOperations() and self.isSurroundedByParenthesis()):
            self.removeOuterParenthesis()