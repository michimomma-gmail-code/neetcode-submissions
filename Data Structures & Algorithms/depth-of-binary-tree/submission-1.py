# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth0(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            h = max(left, right) 

            return h + 1

        return dfs(root)

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        queue = deque([root])
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return level