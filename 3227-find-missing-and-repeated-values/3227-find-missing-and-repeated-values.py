class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        total = n * n

        actual_sum = 0
        actual_square_sum = 0

        for row in grid:
            for x in row:
                actual_sum += x
                actual_square_sum += x * x

        expected_sum = total * (total + 1) // 2
        expected_square_sum = total * (total + 1) * (2 * total + 1) // 6

        diff = actual_sum - expected_sum
        square_diff = actual_square_sum - expected_square_sum

        sum_dm = square_diff // diff

        duplicate = (diff + sum_dm) // 2
        missing = sum_dm - duplicate

        return [duplicate, missing]