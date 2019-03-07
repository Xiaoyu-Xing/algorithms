class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower = []   # Max heap
        self.higher = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.lower) == len(self.higher):
            heapq.heappush(self.lower, -heapq.heappushpop(self.higher, num))
        else:
            heapq.heappush(self.higher, -heapq.heappushpop(self.lower, -num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lower) == len(self.higher):
            return float(-self.lower[0] + self.higher[0]) / 2
        else:
            return float(-self.lower[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
