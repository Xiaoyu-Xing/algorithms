from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            ans[tuple(count)].append(s)
        ret = [v for v in ans.values()]
        return ret


solver = Solution()
print(solver.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
