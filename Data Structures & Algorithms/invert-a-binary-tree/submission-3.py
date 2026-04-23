# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree0(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not root:
                return None
            
            node.right, node.left  = dfs(node.left), dfs(node.right)

            return node

        return dfs(root)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
        
            