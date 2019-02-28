# Array, binary search, divide and conquer
# https://www.youtube.com/watch?time_continue=178&v=LPFhl65R7ww

# O(log(m+n)) time complexity
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i
            # print(m, n, i, j)
            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == m else nums1[i]
            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                high = i - 1
            else:
                low = i + 1

# O(m+n) time complexity
# Merge the two sorted list then find the mid
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first = 0
        second = 0
        x, y = len(nums1), len(nums2)
        final = []
        odd = (x + y) % 2
        mid = (x + y) // 2
        
        while first < x and second < y:
            if nums1[first] < nums2[second]:
                final.append(nums1[first])
                first += 1
            else:
                final.append(nums2[second])
                second += 1
            if len(final) == mid + 1:
                return final[mid] if odd else (final[mid] + final[mid-1]) / 2
        # print(final)
        final += nums1[first:] + nums2[second:]
        # print(final, mid)
        return final[mid] if odd else (final[mid] + final[mid-1]) / 2
            
                
