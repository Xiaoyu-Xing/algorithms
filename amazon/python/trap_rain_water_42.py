# Array, two pointers
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        left_max = right_max = 0
        ans = left = 0
        right = len(height) - 1
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
