class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        l = []
        while top <= bottom and left <= right:
            l.extend(matrix[top][left:right + 1])
            top += 1
            for i in range(top, bottom + 1):
                l.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                l.extend(matrix[bottom][left:right + 1][::-1])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    l.append(matrix[i][left])
                left += 1
        return l