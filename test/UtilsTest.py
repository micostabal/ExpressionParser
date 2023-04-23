import unittest
from src.Utils import charWithDepthsIndexes, splitInIndexes

class UtiliTest(unittest.TestCase):
  def test_charWithDepthsIndexes_f1(self):
    sentence = "(23+45) + 56 + ((45*8)+4)*5"
    self.assertEqual(
      charWithDepthsIndexes(sentence, "+", 0),
      [8, 13]
    )
    
  def test_charWithDepthsIndexes_f2(self):
    sentence = "23*45 + 56 + 45*8+   4+5"
    self.assertEqual(
      charWithDepthsIndexes(sentence, "+", 0),
      [6, 11, 17, 22]
    )
  
  def test_charWithDepthsIndexes_f3(self):
    sentence = "(1+1)*5*7*34358358*(66+6)"
    self.assertEqual(
      charWithDepthsIndexes(sentence, "+", 0),
      []
    )

  def test_splitInIndexes_f1(self):
    sentence="0123456789"
    result=splitInIndexes(sentence, [2, 6])
    self.assertEqual(result, ["01", "345", "789"])

if __name__ == '__main__':
    unittest.main()