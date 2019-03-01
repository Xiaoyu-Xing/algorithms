# Recursive
# Key point: use head.next.next = head this for a circle to point to head itself


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        r = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return r


# Iterative
# Key point: use last to point to previous node, and initialize to None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp
        return last
