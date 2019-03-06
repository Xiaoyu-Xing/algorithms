# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# Similar to greedy meeting room, without the priority queue.
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals or len(intervals) == 1:
            return intervals
        new_intervals = sorted(intervals, key=lambda x: x.start)
        merged = []
        merged.append(new_intervals[0])
        for each in new_intervals[1:]:
            if each.start <= merged[-1].end:
                # Note: need to take max, we don't know
                # whether this one is later or last one is later by end time.
                merged[-1].end = max(merged[-1].end, each.end)
            else:
                merged.append(each)

        return merged
