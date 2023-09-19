# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # # time complexity: O(n)
        # # space complexity: O(n)

        # # get values to a list
        # nums = []
        # while head:
        #     nums.append(head.val)
        #     head = head.next
            
        # # check palindrome
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        # time complexity: O(n)
        # space complexity: O(1)

        slow, fast = head, head

        # find the middle of the list - slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
