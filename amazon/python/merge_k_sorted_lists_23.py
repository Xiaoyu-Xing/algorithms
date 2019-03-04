# Linked list, my method: over time, O(n*k), n = len(lists),
# k is number of elements in the longest linkedlist


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    length = len(lists)
    ans = start = ListNode(0)
    # Test if every linked list reach its end
    while sum([i is None for i in lists]) != length:
        # Get a list of current values of every node, inf if none
        curr = [int(lists[i].val) if lists[i]
                else math.inf for i in range(length)]
        min_index = curr.index(min(curr))
        start.next = lists[min_index]
        start = start.next
        lists[min_index] = lists[min_index].next
    return ans.next


# Linked list with reduce() function, my method: time 4 s
# O(n*total length of every linked list)

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return
        from functools import reduce
        return reduce(self.merge2Lists, lists)

    def merge2Lists(self, l1, l2):
        start = current = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        return start.next


# Divide and conquer, no need to go through all nodes N in every list
# Just need to go through every time merge, total logK levels

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        if not amount:
            return
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def merge2Lists(self, l1, l2):
        start = current = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        return start.next


# Aother one with same divide and conquer.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.merge2lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def merge2lists(self, list1, list2):
        ret = ListNode(0)
        dummy = ret
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        dummy.next = list1 or list2
        return ret.next


# by using heapq to take the min node each time
# why heapify cost O(n): https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        pq = []
        counter = 0  # to prevent heapq compare objects directly

        for li in lists:
            if li:
                heapq.heappush(pq, (li.val, counter, li))
                # or could replace counter with id(li), which get the memory address for the object
                counter += 1
        ret = ListNode(0)
        dummy = ret
        while pq:
            val, _, curr_list = heapq.heappop(pq)
            dummy.next = ListNode(val)
            dummy = dummy.next
            curr_list = curr_list.next
            if curr_list:
                heapq.heappush(pq, (curr_list.val, counter, curr_list))
                counter += 1
        return ret.next


# Or by PriorityQueue (which implemented by heapq), it also either build the counter to prevent compare object
# Or use wrapper class to implement __lt__ method
from queue import PriorityQueue


class Solution():
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        class Wrapper():
            def __init__(self, node):
                self.node = node

            def __lt__(self, other):
                return self.node.val < other.node.val

        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Wrapper(l))
        while not q.empty():
            node = q.get().node
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put(Wrapper(node))
        return head.next
