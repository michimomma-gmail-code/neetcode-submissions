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
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            # for this node, total can be 1) sum of self + left + right, or self + left or right
            # for 1) don't return as it is the end

            # 1)
            terminal = node.val
            if left and left > 0:
                terminal += left
            if right and right > 0:
                terminal += right
            self.maxval = max(self.maxval, terminal)

            # 2)
            tot = node.val
            if left and right:
                tot += max(left, right, 0)
            elif left:
                tot += max(left, 0)
            elif right:
                tot += max(right, 0)

            self.maxval = max(self.maxval, tot)

            return tot        

        dfs(root)
        return self.maxval
            
            