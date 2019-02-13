# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# Greedy, sorted by start time, arrange as many as possible meeting at the same room
# without confilcts of next start time with last end time
# Priority queue with end time in it.
import heapq


class Solution:
    def minMeetingRooms(self, intervals: 'List[Interval]') -> 'int':
        if not intervals:
            return 0
        rooms = []
        intervals.sort(key=lambda x: x.start)
        heapq.heappush(rooms, intervals[0].end)
        for i in intervals[1:]:
            if rooms[0] <= i.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i.end)
        return len(rooms)
