import unittest
from src.Expression import Expression
from src.operations.Sum import Sum
from src.OperationSplitter import OperationSplitter


class OperationSplitterTest(unittest.TestCase):
    splitter = OperationSplitter()
    
    def test_splitter_f1(self):
        sentence = "(3+4) * 34 + 1 + 2 * (45 + 45)"
        
        splitResult = OperationSplitterTest.splitter.splitExpression(Expression(sentence), Sum())
        
        self.assertEqual(splitResult.expressions.__len__(), 3)
        print(list(map(lambda x: x.sentence, splitResult.expressions)))
        self.assertEqual(splitResult.expressions[0].sentence, "(3+4) * 34")
        self.assertEqual(splitResult.expressions[1].sentence, "1")
        self.assertEqual(splitResult.expressions[2].sentence, "2 * (45 + 45)")
        

if __name__ == '__main__':
    unittest.main()