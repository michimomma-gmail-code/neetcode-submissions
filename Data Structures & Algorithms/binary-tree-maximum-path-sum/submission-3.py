# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxval = -float('infinity')
        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # for this node, total can be 1) sum of self + left + right, or self + left or right
            # for 1) don't return as it is the end

            # 1)
            terminal = node.val + left + right

            # 2)
            tot = node.val + max(left, right, 0)
            self.maxval = max(self.maxval, tot, terminal)

            return tot        

        dfs(root)
        return self.maxval
            
            