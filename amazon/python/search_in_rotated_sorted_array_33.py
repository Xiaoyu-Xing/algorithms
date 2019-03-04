# Do binary search directly, doesn't care the pivot point
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


# Second solution:
# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
# The most important observation is the "If nums[mid] and target are "on the same side" of nums[0], just take nums[mid]
def search(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if (nums[mid] < nums[0]) == (target < nums[0]):
            if (nums[mid] < target):
                lo = mid + 1
            elif (nums[mid] > target):
                hi = mid
            else:
                return mid
        elif target < nums[0]:
            lo = mid + 1
        else:
            hi = mid
    return -1


# Calculate pivot point first, then do binary search depends on target
pass


# Normal binary search
def binary_search(arr, low, high, target):
    # Need to include = here, e.g. [5], target = 5, if not, wrong answer
    # then the high and low need to be modified both,
    # e.g. if low==high, and it falls the same if condition, then forever loop
    while low <= high:
        mid = (low + high) // 2
        print(low, high, mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_recurrsive(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > x:
            return binary_search_recurrsive(arr, low, mid - 1, target)
        else:
            return binary_search_recurrsive(arr, mid + 1, high, target)


arr = [2, 3, 4, 10, 40]
arr1 = [-1, 0, 3, 5, 9, 12]
arr2 = [5]
arr3 = [-1, 0, 3, 5, 9, 12]

x = 10
x1 = 2
x2 = 5
x3 = 2
print(search(arr3, x3))
