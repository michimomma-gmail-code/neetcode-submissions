# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if left and right:
            return True
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def isSameTree(self, p, q):


        def dfs(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            

            l = dfs(p.left, q.left)
            r = dfs(p.right, q.right)

            if p.val == q.val and l and r:
                return True

            return False


        return dfs(p, q)




















