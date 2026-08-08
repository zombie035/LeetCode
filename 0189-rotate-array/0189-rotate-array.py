class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0: return

        left, right = nums[:-k], nums[-k:]
        nums[:k] = right
        nums[k:] = left 
        
