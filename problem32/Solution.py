# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev, nex, fast, maxSum = None, head.next, head.next.next, 0
        # Reverse first-half of the linkedlist
        while fast:
            head.next = prev
            prev = head
            head = nex
            nex = nex.next
            fast = fast.next.next
        head.next = prev
        # traverse through 2 linkedlists
        while head:
            pairSum = head.val + nex.val
            maxSum = max(pairSum, maxSum)
            head = head.next
            nex = nex.next
        return maxSum
