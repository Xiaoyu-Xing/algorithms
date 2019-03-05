# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)


class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        left_min_index = [-1] * len(heights)
        right_min_index = [-1] * len(heights)
        # Imagin the -1 position is a column of height of 0
        left_min_index[0] = -1
        # Imagin the len(heights) position is a column with height of 0
        right_min_index[-1] = len(heights)

        for i in range(1, len(heights)):
            prev = i - 1
            # If the i position height <= than previous height, the there is no constraint from previous column, so look even further to the constraint of the previous column, until reach the far left
            while prev >= 0 and heights[i] <= heights[prev]:
                prev = left_min_index[prev]
            # Notice we overmoved one position here
            left_min_index[i] = prev

        for i in range(len(heights) - 2, -1, -1):
            prev_right = i + 1
            while prev_right <= len(heights) - 1 and heights[i] <= heights[prev_right]:
                prev_right = right_min_index[prev_right]
            # Notice we also overmoved one position here
            right_min_index[i] = prev_right

        res = 0
        for i in range(len(heights)):
            res = max(res,
                      heights[i] * (right_min_index[i] - left_min_index[i] - 1))
        return res


solver = Solution()
print(solver.largestRectangleArea([2, 1, 5, 6, 2, 3]))

# Stack method O(n)
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms


def largestRectangleArea(height):
    # Two fake element, to denote the start and end
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        # When the next enstack element is smaller, calculate areas for previous elements,
        # because new constaint come in.
        # Until old but smaller element shows.
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            # Because the i and stack[-1] is outside of the caculated area
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    # restore the pass-in arguments
    height.pop()
    return ans


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))


# Divide and conquer time O(nlogn), n is length of list,
# worst cae O(n^2) if pivot is always in ends, similar to quick sort
def max_area_histogram(heights):
    def max_area(heights, start, end):
        if start > end:
            return 0
        # find the index of the smallest number in current slice
        # Notice the index() function second arguments
        # MIN_Index = heights.index(min(heights[start:end + 1]), start)
        # Alternatively, find the MIN_Index manually
        MIN_Index = start
        for i in range(start, end + 1):
            if heights[i] < heights[MIN_Index]:
                MIN_Index = i
        ret = max(heights[MIN_Index] * (end - start + 1),
                  max_area(heights, start, MIN_Index - 1),
                  max_area(heights, MIN_Index + 1, end))
        return ret
    return max_area(heights, 0, len(heights) - 1)


print(max_area_histogram([2, 1, 5, 6, 2, 3]))

# O(n^2) method, by memorize the minimum value in both side


def max_are_n_squre(heights):
    ans = 0
    for i in range(len(heights)):
        range_min = heights[i]
        for j in range(i, len(heights)):
            range_min = min(range_min, heights[j])
            ans = max(ans, (j - i + 1) * range_min)
    return ans


print(max_are_n_squre([2, 1, 5, 6, 2, 3]))
