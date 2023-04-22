import unittest
from src.OperationSplitter import OperationSplitter, charWithDepthsIndexes

class OperationSplitterTest(unittest.TestCase):
    
    def test_charWithDepthsIndexes_f1(self):
        sentence = "(23+45) + 56 + ((45*8)+4)*5"
        
        self.assertEqual(
            charWithDepthsIndexes(sentence, "+", 0),
            [8, 13]
        )


if __name__ == '__main__':
    unittest.main()