# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal0(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        res = []
        cur = root

        last_visited = None

        while cur or stack:

            while cur:
                stack.append(cur)
                cur = cur.left

            peak_node = stack[-1]

            if peak_node.right and last_visited != peak_node.right:
                cur = peak_node.right
            else:
                res.append(peak_node.val)
                last_visited = stack.pop()

        
        return res

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
            stack = [root]
            res = []

            while stack:
                node = stack.pop()
                if node:
                    res.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)

            res = res[::-1]            

            return res
