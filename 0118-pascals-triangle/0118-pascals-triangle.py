from math import comb

class Solution:
    def generate(self, numRows: int):
        l = []

        for i in range(numRows):
            row = []
            for r in range(i + 1):
                row.append(comb(i, r))
            l.append(row)

        return l