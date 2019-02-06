public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode start = new ListNode(0);
    ListNode ans = start;
    while(l2 != null && l1 != null) {
        if(l1.val < l2.val) {
            start.next = l1;
            l1 = l1.next;
        } else {
            start.next = l2;
            l2 = l2.next;
        }
        start = start.next;
    }
    if (l1 != null) {
        start.next = l1;
    } else if (l2 != null) {
        start.next = l2;
    }
    return ans.next;
}

// Or
public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    if (l1 == null) {
        return l2;
    } else if (l2 == null) {
        return l1;
    } else if (l1.val < l2.val) {
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    } else if (l1.val >= l2.val) {
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
}