# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes0(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        if not root:
            return None    

        def dfs(node, parent):
            if not node:
                return 

            dfs(node.left, node)
            dfs(node.right, node)

            if node.val == target and not node.left and not node.right:
                if not parent:
#                    print(root == node)
#                    node = None
                    return
                elif parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None

            return
        dummy = TreeNode()
        dummy.left = root            
        dfs(dummy, None)
        return dummy.left

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        
        return root

