import unittest
from src.ExpressionParser import ExpressionParser
from src.SingleTokenEvaluator import SingleTokenEvaluator
from src.OperationSplitter import OperationSplitter
from src.operations.Operations import OPERATIONS
from src.Expression import Expression

class ExpressionParserTest(unittest.TestCase):
    parser: ExpressionParser = ExpressionParser(
        OperationSplitter(),
        SingleTokenEvaluator({}),
        OPERATIONS
    )
    
    def test_simpleExpression_f1(self):
        expression = Expression(" 1 * (3+4)*4")
        
        result = ExpressionParserTest.parser.evaluate(expression)
        
        self.assertEqual(result, 28)
    
    def test_simpleExpression_f2(self):
        expression = Expression("  1 +    (1*1)*(6+1)")
        
        result = ExpressionParserTest.parser.evaluate(expression)
        
        self.assertEqual(result, 8)

    def test_simpleExpression_f3(self):
        expression = Expression(" 3*3*3+3")
        
        result = ExpressionParserTest.parser.evaluate(expression)
        
        self.assertEqual(result, 30)

    def test_simpleExpression_f4(self):
        expression = Expression("(1+1)*(1+1)*(1+1)*(1+1)")
        
        result = ExpressionParserTest.parser.evaluate(expression)
        
        self.assertEqual(result, 16)

    def test_simpleExpression_f5(self):
        expression = Expression("(((((5)))))")
        
        result = ExpressionParserTest.parser.evaluate(expression)
        
        self.assertEqual(result, 5)

    def test_simpleExpression_f6(self):
        expression = Expression("((((4))))*((3))*((8))")
        
        result = ExpressionParserTest.parser.evaluate(expression)
        
        self.assertEqual(result, 96)

    def test_simpleExpression_f7(self):
        expression = Expression("1 + 2*3")
        
        result = ExpressionParserTest.parser.evaluate(expression)
        
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()