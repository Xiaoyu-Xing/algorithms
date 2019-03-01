"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        old = head
        while old:
            new = Node(old.val, None, None)
            new.next = old.next
            old.next = new
            old = new.next
        old = head
        while old:
            old.next.random = old.random.next if old.random else None
            old = old.next.next
        old = head
        new = head.next
        ret = head.next
        while old:
            old.next = new.next
            new.next = old.next.next if old.next else None
            old = old.next
            new = new.next
        return ret
