# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal0(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def dfs(node):
 #           res = []
            if not node:
                return
#            res.append(node.val)
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        cur = root
        res = []
        while cur or stack:

            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res
