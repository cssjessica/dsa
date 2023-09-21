# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # two pointers
        # time complexity: O(n)
        # space complexity: O(1)

        # left pointer
        cur = head
        for i in range(k - 1):
            cur = cur.next
        left = cur

        # right pointer
        right = head
        while cur.next:
            cur = cur.next
            right = right.next
            
        # swap values
        left.val, right.val = right.val, left.val

        return head
