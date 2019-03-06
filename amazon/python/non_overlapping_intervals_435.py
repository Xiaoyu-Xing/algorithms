# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals: List[Interval]) -> int:
        if not intervals or len(intervals) == 1:
            return 0
        # Sort based on start time
        new_intervals = sorted(intervals, key=lambda x: x.start)
        count = 0
        prev_end = new_intervals[0].end
        for each in new_intervals[1:]:
            # If overlapping, keep the one with earlier end time, and delete another one
            if each.start < prev_end:
                count += 1
                prev_end = min(each.end, prev_end)
            # Otherwise, no overlapping, update the previous ending time with the current one
            else:
                prev_end = each.end
        return count