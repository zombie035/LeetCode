class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = []
        for i in range(rowIndex+1):
            x = comb(rowIndex,i)
            l.append(x)
        return l
    def factorial(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def comb(x, y):
        if y < 0 or y > x:
            return 0  # or raise error
        return factorial(x) // (factorial(y) * factorial(x - y))