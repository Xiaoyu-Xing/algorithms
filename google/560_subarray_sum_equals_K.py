class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':

        dic = {0: 1}
        ans = total = 0
        for i in nums:
            total += i
            ans += dic.get(total - k, 0)
            dic[total] = dic.get(total, 0) + 1
        return ans
