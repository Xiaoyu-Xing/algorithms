# Reservoir sampling
# Explain: https://leetcode.com/problems/random-pick-index/discuss/88071/C%2B%2B_Time%3A-O(n)-Space%3A-O(n)_116ms_96.41_with-clear-explanation-by-probability
# Explain: https://leetcode.com/problems/random-pick-index/discuss/88072/Simple-Reservoir-Sampling-solution


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                # Key: the probability to choose the current index is: 1/(count)
                if chance == count:
                    res = i
        return res
