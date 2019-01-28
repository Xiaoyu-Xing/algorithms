// https://www.youtube.com/watch?v=8BHqSdwyODs
// Array, two points
class Solution {
    public int trap(int[] height) {
        int leftMax = 0, rightMax = 0, ans = 0;
        int left = 0, right = height.length - 1;
        while (left < right) {
            leftMax = Math.max(height[left], leftMax);
            rightMax = Math.max(height[right], rightMax);
            if (leftMax < rightMax) {
                ans += leftMax - height[left];
                left++;
            } else {
                ans += rightMax - height[right];
                right--;
            }
        }
        return ans;
    }
}