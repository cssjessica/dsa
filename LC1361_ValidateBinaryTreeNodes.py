class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # time complexity: O(n)
        # space complexity: O(n)
        # valid binary tree: - connected - no cycle - undirected

        # check if there's a root
        hasParent = set(leftChild + rightChild)
        hasParent.discard(-1)
        if len(hasParent) == n:
            return False

        # get the root	
        root = -1
        for i in range(n):
            if i not in hasParent:
                root = i
                break
                
        visit = set()
        def dfs(i):
            if i == -1:
                return True
            # cycle	
            if i in visit:
                return False
            visit.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])
            
        # all nodes connected
        return dfs(root) and len(visit) == n
