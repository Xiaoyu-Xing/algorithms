# Shuffle is faster than pop

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.copy = nums

        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.copy

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ans = self.copy[:]
        length = len(self.copy)
        for i in range(length):
            swap = random.randrange(i, length)
            ans[i], ans[swap] = ans[swap], ans[i]
        return ans
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()






# pop method: O(n**2)
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.copy = nums

        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.copy

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums_copy = self.copy[:]
        ans = []
        length = len(self.copy)
        for i in range(length):
            to_be_removed = random.randrange(len(nums_copy))
            ans.append(nums_copy.pop(to_be_removed))
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()