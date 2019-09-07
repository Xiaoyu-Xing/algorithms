"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """

    def insert(self, intervals, newInterval):
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]
        new_result = []
        insert_pos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                new_result.append(interval)
                insert_pos += 1
            elif newInterval.end < interval.start:
                new_result.append(interval)
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
        new_result.insert(insert_pos, newInterval)
        return new_result
