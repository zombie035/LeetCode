class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        curr = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                num = nums[i] + nums[left] + nums[right]

                # Update closest sum
                if abs(target - num) < abs(target - curr):
                    curr = num

                # If exact target is found
                if num == target:
                    return num

                # Need a larger sum
                elif num < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return curr