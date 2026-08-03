class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        l = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:

            # Top
            for i in range(left, right + 1):
                l[top][i] = num
                num += 1
            top += 1

            # Right
            for i in range(top, bottom + 1):
                l[i][right] = num
                num += 1
            right -= 1

            # Bottom
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    l[bottom][i] = num
                    num += 1
                bottom -= 1

            # Left
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    l[i][left] = num
                    num += 1
                left += 1

        return l