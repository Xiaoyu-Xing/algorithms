# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 2 passes, 1st to find the lenght, 2nd to delete
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Key is to create a dummy head
        # So the edge case, e.g. delete the head, will be easy
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        if n > count:
            return None
        curr = dummy
        # move pointer to the previous one before the deleted one
        for i in range(count - n):
            curr = curr.next
        # Cross over the deleted one
        curr.next = curr.next.next
        return dummy.next



# One pass:
# Key point: 1. create dummy head for edge case 2. move first pointer n steps ahead
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        while n + 1:
            first = first.next
            n -= 1
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next