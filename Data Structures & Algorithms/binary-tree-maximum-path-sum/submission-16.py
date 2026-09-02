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
            


    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_cum = root.val

        def dfs(node):
            nonlocal max_cum

            if not node:
                return 0
#            max_cum = max(max_cum, cum)
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            sub_res = max(left, right) + node.val
#            print(sub_res, node.val, left, right)
            max_cum = max(max_cum, sub_res, left + right + node.val)
            return sub_res

        res = dfs(root)
        return max_cum










































            