# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        # A left leaf node meets two constraits
        # It has no children nodes
        # It is the left node to the node above it

        def recurse(node):
            if node == None:
                return 0
            add = 0
            if node.left and (node.left.left == None and node.left.right == None):
                add += node.left.val
                
            return add + recurse(node.left) + recurse(node.right)
            
        return recurse(root)
