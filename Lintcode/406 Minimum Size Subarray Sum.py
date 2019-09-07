
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums, s):
        if s <= 0:
            return 1 if nums else -1
        left = 0
        min_length = float("inf")
        total = 0
        for right, num in enumerate(nums):
            total += num
            while total >= s:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1
        return min_length if min_length != float("inf") else -1
