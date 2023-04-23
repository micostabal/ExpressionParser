from typing import List

def charWithDepthsIndexes(sentence: str, targetChar: str, depth: int) -> List[int]:
  currentDepth=0
  indexes=[]
  for index, char in enumerate(sentence):
    if char=='(':
      currentDepth+=1
    elif char==")":
      currentDepth-=1
    elif char==targetChar and depth==currentDepth:
      indexes.append(index)
  return indexes

def splitInIndexes(sentence: str, indexes: List[int]):
  if len(indexes)==0:
    return [sentence]
  return [sentence[i:j].strip(" ") if i==0 else sentence[i+1:j].strip(" ")
   for i,j in zip([0]+indexes, indexes+[None])]