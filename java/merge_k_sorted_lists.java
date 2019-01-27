/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        int length = lists.length;
        if(length == 0) return null;
        int interval = 1;
        while(interval < length) {
        	for(int i = 0; i < length - interval; i += interval*2) {
        		lists[i] = merge2Lists(lists[i], lists[i+interval]);
        	}
        	interval = interval*2;
        }
        return lists[0];
        
    }
    public ListNode merge2Lists(ListNode l1, ListNode l2){
    	ListNode start = new ListNode(0);
    	ListNode curr = start;
    	while (l1 != null && l2 != null){
    		if(l1.val < l2.val) {
    			curr.next = l1;
    			l1 = l1.next;
    		} else {
    			curr.next = l2;
    			l2 = l2.next;
    		}
    		curr = curr.next;
    	}
    	if(l1 != null) {
    		curr = l1;
    	} else {
    		curr = l2;
    	}
    	return start.next;
    }
}