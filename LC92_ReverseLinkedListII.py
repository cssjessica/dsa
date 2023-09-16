# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # 1. reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
            
        # Now leftPrev = "node before left" and cur = "left"
        # 2. reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev = cur
            cur = tmpNext

        # 3. update pointers
        # new tail of the left-right linked list
        # cur is at the node after right
        leftPrev.next.next = cur
        # new head of the left-right linked list
        # prev is at the right node
        leftPrev.next = prev

        return dummy.next
