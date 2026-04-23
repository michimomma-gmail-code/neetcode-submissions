# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, node):
        if not node:
            return 0

        left = self.getHeight(node.left)
        right = self.getHeight(node.right)

        return max(left, right) +1   

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True


        h_right = self.getHeight(root.right)
        h_left = self.getHeight(root.left)

        if abs(h_right - h_left) > 1:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        
