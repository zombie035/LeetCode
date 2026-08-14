class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        loop = 0
        result = sum(grid, [])        
        n = len(result)
        actual_sum = 0
        actual_square_sum = 0
        #finding the missing number
        for x in result:
            actual_sum += x
            actual_square_sum += x * x

        expected_sum = n * (n + 1) // 2
        expected_square_sum = n * (n + 1) * (2 * n + 1) // 6

        diff = actual_sum - expected_sum
        square_diff = actual_square_sum - expected_square_sum

        sum_dm = square_diff // diff

        a = (diff + sum_dm) // 2
        b = sum_dm - a
        l = [a,b]
        return l
