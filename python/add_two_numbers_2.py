# Linked list, math
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    if l1 is None or l2 is None:
        return l1 or l2
    # if given lists are from high order to low order
    # l1 = reverse_list(l1)
    # l2 = reverse_list(l2)
    result = None
    current = None
    carry = False
    while l1 and l2:
        if not result:
            current = result = ListNode(0)
        else:
            current.next = ListNode(0)
            current = current.next
        temp = l1.val + l2.val + carry
        l1 = l1.next
        l2 = l2.next
        carry = False
        if temp >= 10:
            carry = True
        current.val = temp % 10
    left = l1 or l2
    while left:
        current.next = ListNode(0)
        current = current.next
        temp = carry + left.val
        carry = False
        if temp >= 10:
            carry = True
        current.val = temp % 10
        left = left.next
    if carry:
        current.next = ListNode(int(carry))
    return result


def reverse_list(l):
    if not l:
        return
    start = l
    current = start
    previous = None
    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    return previous


# Better idea: less control code, add whatever exists
def addTwoNumbers(l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10
    return dummy.next
