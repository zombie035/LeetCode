class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2

            left, count_left = merge_sort(arr[:mid])
            right, count_right = merge_sort(arr[mid:])

            count = count_left + count_right

            # Count reverse pairs across left and right
            j = 0

            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1

                count += j

            # Normal merge
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, count

        _, count = merge_sort(nums)
        return count