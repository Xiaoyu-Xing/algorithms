# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# O(1) space, O(n) time
# idea: the fast pointer is 1 step faster than the slow, 
# so if cycle, the fast will catch up slow and meet
# Due to the 1 step difference, the fast won't cross the slow pointer
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        