# Similar to longest substring with k different characters, with k = 2
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree or len(tree) == 0:
            return 0
        left = 0
        ans = 0
        baskets = {}
        # Use the dictionary to store the last index all fruits/letters in the array
        for t, fruit in enumerate(tree):
            baskets[fruit] = t
            if len(baskets) > 2:
                left = min(baskets.values())
                del baskets[tree[left]]
                left += 1
            ans = max(ans, t - left + 1)
        return ans
