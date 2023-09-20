# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse 1st half of the linked list to go outward

        slow, fast = head, head
        prev = None

        # get to the middle of the list while reverse the first half
        while fast and fast.next:
            fast = fast.next.next
            # reverse
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        # compute sums
        res = 0
        # slow is at the first node of the second half
        # prev is at the last node of the first half that has been reversed
        while slow:
            res = max(res, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
            
        return res
