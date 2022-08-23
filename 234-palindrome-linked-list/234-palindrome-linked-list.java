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
    public boolean isPalindrome(ListNode head) {
        ArrayList<Integer> nums = new ArrayList<>();
        ListNode pointer = head;
        while(pointer != null) {
            nums.add(pointer.val);
            pointer = pointer.next;
        }
        int start = 0, end = nums.size() - 1;
        boolean palindrome = true;
        while(start<=end) {
            if(nums.get(start) != nums.get(end)) {
                palindrome = false;
                break;
            }
            start++;
            end--;
        }
        return palindrome;
    }
}