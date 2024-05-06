# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stack = []
        # cur = head
        # while cur:
        #     while stack and cur.val > stack[-1]:
        #         stack.pop()
        #     stack.append(cur.val)
        #     cur = cur.next
            
        # dummy = ListNode()
        # cur = dummy
        # for n in stack:
        #     cur.next = ListNode(n)
        #     cur = cur.next
        # return dummy.next


        def reverse(head):
            prev, cur = None, head
            while cur:	
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            return prev

        head = reverse(head)
        cur = head
        cur_max = cur.val
        while cur.next:
        	if cur.next.val < cur_max:
        		cur.next = cur.next.next
        	else:
        		cur_max = cur.next.val
        		cur = cur.next
        return reverse(head)
