class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """

    def findMissingRanges(self, nums, lower, upper):
        if not nums:
            if lower == upper:
                return [str(lower)]
            elif lower < upper:
                return [str(lower) + "->" + str(upper)]
        prev = lower
        result = []
        for num in nums:
            end = num - 1
            if end > prev:
                result.append(str(prev) + "->" + str(end))
            elif end == prev:
                result.append(str(prev))
            prev = num + 1
        if prev < upper:
            result.append(str(prev) + "->" + str(upper))
        elif prev == upper:
            result.append(str(upper))
        return result


class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """

    def findMissingRanges(self, nums, lower, upper):
        if not nums:
            return [self.get_range_string(lower, upper)]
        prev = lower
        result = []
        for num in nums:
            end = num - 1
            new_interval = self.get_range_string(prev, end)
            if new_interval:
                result.append(new_interval)
            prev = num + 1
        new_interval = self.get_range_string(prev, upper)
        if new_interval:
            result.append(new_interval)
        return result

    def get_range_string(self, low, high):
        if low == high:
            return str(low)
        elif low < high:
            return str(low) + "->" + str(high)
