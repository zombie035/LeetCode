from math import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = []
        
        for i in range(rowIndex+1):
            x = comb(rowIndex,i)
            l.append(x)
        return l