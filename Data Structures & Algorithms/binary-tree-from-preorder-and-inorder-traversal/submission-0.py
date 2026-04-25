# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder: 2 is leaf node. next node is parent 
        #          1 is parent of 2. next node is parent or left child. know 1 is root. so left child
        #          3. next node is left child, parent or right child. 
        # for each node in preorder (root for each iteration)
        # know left and right sides (don't know which is direct child)
        #
        #   
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1 :])
        
        return root


