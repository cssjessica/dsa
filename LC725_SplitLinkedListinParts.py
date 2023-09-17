# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, cur = 0, head

        # get size
        while cur:
            cur = cur.next
            length += 1

        # get size of the splited lists
        base_len, extra_len = length // k, length % k
        cur = head
        res = []

        # split lists
        for i in range(k):
            res.append(cur)
            
            for j in range(base_len - 1 + (1 if extra_len else 0)):
                if not cur: break
                cur = cur.next
            extra_len -= (1 if extra_len else 0)
            if cur:
                cur.next, cur = None, cur.next
        return res
