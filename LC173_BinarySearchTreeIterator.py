# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.helper(root)

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        self.helper(cur)
        return res.val
        
    def hasNext(self) -> bool:
        return self.stack != []
        

    def helper(self, tree):
        while tree:
            self.stack.append(tree)
            tree = tree.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
