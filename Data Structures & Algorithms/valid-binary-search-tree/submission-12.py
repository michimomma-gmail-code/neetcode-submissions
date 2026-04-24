# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lb, ub):
            if not root:
                return True

            if not lb < root.val < ub:
                return False

            left = dfs(root.left, lb, root.val)
            right = dfs(root.right, root.val, ub)
    
            if left and right:
                return True
            else:
                return False

        res = dfs(root, -float('infinity'), float('infinity'))

        return res

