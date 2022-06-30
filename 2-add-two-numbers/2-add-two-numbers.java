/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode start = new ListNode();
        int val = 0, sum = 0, carry = 0;
        ListNode currentpoint= new ListNode();
        start.next = currentpoint;
        do{
            ListNode current = new ListNode(0, null);
            int l1_val = 0, l2_val = 0;
            boolean flag_l1 = (l1==null)?false:true;
            boolean flag_l2= (l2==null)?false:true;
            
            if(flag_l1)
                l1_val = l1.val;
            if(flag_l2)
                l2_val = l2.val;
            sum = l1_val + l2_val + carry;
            carry = sum/10;
            val = sum%10;
            current.val = val;
            currentpoint.next = current;
            currentpoint = current;
            
            if(flag_l1) {l1=l1.next;}
            if(flag_l2) {l2=l2.next;}
            
        }while(l1 != null || l2 != null || carry != 0);
        
        return start.next.next;
        
    }
}