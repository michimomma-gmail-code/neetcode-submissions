# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        if not root:
            return Node()            

        def dfs(node, parent):
            if not node:
                return 

            dfs(node.left, node)
            dfs(node.right, node)

            if node.val == target and not node.left and not node.right:
                if not parent:
                    print(root == node)
#                    node = None
                elif parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None

            return
        dummy = TreeNode()
        dummy.left = root            
        dfs(dummy, None)
        return dummy.left
