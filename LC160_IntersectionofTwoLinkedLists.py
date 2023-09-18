# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # # time complexity: O(n+m)
        # # space complexity: O(1)
        # l1, l2 = headA, headB
        # while l1 != l2:
        #     l1 = l1.next if l1 else headB
        #     l2 = l2.next if l2 else headA
        # return l1

        # time complexity: O(n+m)
        # space complexity: O(1)

        # get lengths
        # O(m+n)
        lenA = 0
        listA = headA
        while listA:
            listA = listA.next
            lenA += 1
        lenB = 0
        listB = headB
        while listB:
            listB = listB.next
            lenB += 1       

        # set longer list to the right node for comparison
        # O(max(m,n))
        if lenA > lenB:
            n = lenA - lenB
            while n > 0:
                headA = headA.next
                n -= 1

        if lenB > lenA:
            n = lenB - lenA
            while n > 0:
                headB = headB.next
                n -= 1
        # compare the two lists
        # O(min(m,n))
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return headA

