# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
# reverse
# find element by index
# remove element
# tranverse and retun tail of reverse or head of original


        dummy = ListNode(0, head)
        left = dummy
        right = head

        # initialize right pointer
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # move pointer until right pointer reaches end of linked list
        while right:
            left = left.next
            right = right.next
            
        # delete 
        left.next = left.next.next

        return dummy.next
