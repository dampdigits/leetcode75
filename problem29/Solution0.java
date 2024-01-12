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
    public ListNode deleteMiddle(ListNode head) {
        if(head==null || head.next==null)
            return null;
        
        int length = 0;
        ListNode ans = head, current = head;
        
        while (current != null) {
            length++;
            current = current.next;
        }
        
        int mid = length / 2;
        length = 0;

        while (true) {
            if (length == mid - 1) {
                head.next = (head.next).next;
                break;
            }
            head = head.next;
            length++;
        }
        return ans;
    }
}
