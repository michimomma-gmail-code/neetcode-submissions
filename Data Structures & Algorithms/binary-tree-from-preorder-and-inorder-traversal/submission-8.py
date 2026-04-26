# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        self.pre2in_index = {p : i for i, p in enumerate(inorder)}
        self.p_index = 0

        def dfs(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.p_index]
            root = TreeNode(root_val)

            mid = self.pre2in_index[preorder[self.p_index]]
            self.p_index += 1

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(inorder) - 1)

