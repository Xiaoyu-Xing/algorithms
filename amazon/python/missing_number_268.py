# XOR method:
# see solution 3 on solution of leetcode
# https://leetcode.com/problems/missing-number/solution/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


# For sorted array: better to use binary search
def missing_number_sorted(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    return left
