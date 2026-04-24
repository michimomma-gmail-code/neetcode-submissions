# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        num_good = 0
        def dfs(root, max_v):
            if not root:
                return None
            nonlocal num_good 
            if root.val >= max_v:
                max_v = root.val
                num_good += 1

            left = dfs(root.left, max_v)
            right = dfs(root.right, max_v)

        
        dfs(root, root.val)

        return num_good

        