// Two pointers.
// Closest Target Value
// Given an array, find two numbers in the array and 
// their sum is closest to the target value but does not exceed the target value, 
// return their sum.

public int closestTargetValue(int target, int[] array) {
	int size = array.length;
	Arrays.sort(array);
	if (array[0] > target) return -1;
	int max = Integer.MIN_VALUE, left = 0, right = size - 1;
	while (left < right) {
		int curr = array[left] + array[right];
		if (curr > target) {
			right--;
		} else {
			max = Math.max(max, curr);
			left++;
		}
	}
	if (max == Integer.MIN_VALUE) return -1;
	return max;
}