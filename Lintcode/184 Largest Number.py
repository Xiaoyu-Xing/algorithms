from functools import cmp_to_key


class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        if not nums:
            return ""
        nums = [str(num) for num in nums]
        # Notice: we need to use the cmp_to_key in here because the comparison is not on the certain field of an object
        # , but need a computation from two element, so the multiple calculation is inevitable O(nlogn), so by changing
        # to "key" won't work, since it only has O(n) calculation.
        nums.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        if nums[0] == "0":
            return "0"
        return "".join(nums)
