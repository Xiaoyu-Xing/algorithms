public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode slow=head,fast=head;
        ListNode prev=null;
        while(fast!=null&&fast.next!=null){
            fast=fast.next.next;
            prev=slow;
            slow=slow.next;
        }
        prev.next=reverse(slow);
        return head;
        /*
        OR:
        while(fast.next!=null&&fast.next.next!=null){
            fast=fast.next.next;
            slow=slow.next;
        }
        slow.next=reverse(slow.next);
        return head;
        */
    }
    public ListNode reverse(ListNode head){
        ListNode prev=null;
        while(head!=null){
            ListNode temp=head.next;
            head.next=prev;
            prev=head;
            head=temp;
        }
        return prev;
    }
}