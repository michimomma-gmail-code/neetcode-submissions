# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree0(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #   
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1 :])
        
        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def _buildTree(left, right):
            #   
            if left > right:
                return None

            root = TreeNode(preorder[self.pindex])
            mid = self.inorderindex[preorder[self.pindex]]
            self.pindex += 1

            root.left = _buildTree(left, mid - 1)
            root.right = _buildTree(mid + 1, right)
    #        root.left = self._buildTree(preorder[1 : mid + 1], inorder[:mid])
    #        root.right = self._buildTree(preorder[mid + 1:], inorder[mid + 1 :])
            
            return root


        self.inorderindex = {}
        self.pindex = 0
        # node -> inorder index
        for i, p in enumerate(inorder):
            self.inorderindex[p] = i
        
        return _buildTree(0, len(preorder)-1)
