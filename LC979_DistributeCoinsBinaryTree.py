# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(cur):
            if not cur:
                return 0
                
            l_extra = dfs(cur.left)
            r_extra = dfs(cur.right)
            extra_coins = cur.val - 1 + l_extra + r_extra
            self.res += abs(extra_coins)
            return extra_coins
        dfs(root)
        return self.res
