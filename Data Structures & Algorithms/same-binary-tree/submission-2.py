# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        
        def dfs(p, q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if p and not q:
                return False
            
            if p.val != q.val:
                return False
            left =  dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            if left == False:
                return False
            if right == False:
                return False
            return True

        return dfs(p,q)
            
        