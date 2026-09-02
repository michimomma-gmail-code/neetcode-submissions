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




    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # root = preorder[0] (1)
        # -> left = inorder[0] (2)
        # -> right = inrder[2, 3] (3, 4)
        # 
        # preorder: node val to index in preorder
        #

        preorder_idx = 0
        val2_inorder_idx = {inorder[i]:i  for i in range(len(inorder)) }
#        print(val2_inorder_idx)

        def dfs(inorder_idx_left, inorder_idx_right):
            if inorder_idx_left > inorder_idx_right:
                return None

            nonlocal preorder_idx

            val = preorder[preorder_idx]
            preorder_idx += 1

            root = TreeNode(val)
            mid_idx = val2_inorder_idx[val]            

            root.left = dfs(inorder_idx_left, mid_idx - 1)
            root.right = dfs(mid_idx + 1, inorder_idx_right)
            
            return root

        return dfs(0, len(inorder) - 1)











































