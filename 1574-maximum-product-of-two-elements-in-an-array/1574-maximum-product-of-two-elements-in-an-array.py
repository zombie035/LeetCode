class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)