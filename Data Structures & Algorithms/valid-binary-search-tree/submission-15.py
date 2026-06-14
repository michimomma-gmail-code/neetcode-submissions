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

            if not (lb < root.val < ub):
                return False

            left = dfs(root.left, lb, root.val)
            right = dfs(root.right, root.val, ub)
    
            if left and right:
                return True
            else:
                return False

        res = dfs(root, -float('infinity'), float('infinity'))

        return res




    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node, lb, ub):

            if not node:
                return True

            print(f'lb = {lb}, ub = {ub}, val = {node.val}')

            if node.val <= lb or node.val >= ub:
                return False

            if not dfs(node.left, lb, min(ub, node.val)):
                return False
            if not dfs(node.right, max(lb, node.val), ub):
                return False

            return True


        return dfs(root, -float("infinity"), float("infinity"))








































