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
    public int pairSum(ListNode head) {
        List<Integer> arr = new ArrayList<>();
        int size = 0;
        while (head != null) {
            arr.add(head.val);
            head = head.next;
            size++;
        }
        int maxsum = 0, i = 0;
        while (i < size/2) {
            maxsum = Math.max(maxsum, arr.get(i)+arr.get(size-i-1));
            i++;
        }
        return maxsum;
    }
}
