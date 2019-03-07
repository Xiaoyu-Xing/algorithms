# Good explanation: https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
# Short code: https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.


def rob(nums):
    prev_prev = 0
    prev = 0
    for num in nums:
        temp = prev
        prev = max(prev_prev + num, prev)
        prev_prev = temp
    return prev
