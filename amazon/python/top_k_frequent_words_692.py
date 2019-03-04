import heapq
from collections import defaultdict
from collections import Counter


class Element:
    def __init__(self, word, count):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        return self.count > other.count


class Solution:
    # Method 1, by negative counts for heapq
    def topKFrequent(self, words, k):
        fre = defaultdict(int)
        for word in words:
            fre[word] -= 1
        # string object has __lt__ function, so need to worry equal string
        # it will automaticlaly output the lower alphabetical order
        pq = [(count, word) for word, count in fre.items()]
        heapq.heapify(pq)
        ret = []
        while k:
            ret.append(heapq.heappop(pq)[1])
            k -= 1
        return ret


    # Method 2, by self defined class to facilitate heapq
    def topKFrequentByNewClass(self, words, k):
        fre = Counter(words)
        words_obj = [Element(word, count) for word, count in fre.items()]
        heapq.heapify(words_obj)
        ret = []
        while k:
            ret.append(heapq.heappop(words_obj).word)
            k -= 1
        return ret


solver = Solution()
print(solver.topKFrequent(
    ["the", "day", "is", "sunny", "is", "the", "the", "the", "sunny", "is", "is"], 4))


print(solver.topKFrequentByNewClass(
    ["the", "day", "is", "sunny", "is", "the", "the", "the", "sunny", "is", "is"], 4))
