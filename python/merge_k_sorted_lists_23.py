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
