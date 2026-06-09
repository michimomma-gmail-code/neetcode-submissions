# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertNode(self, root: Optional[TreeNode], newnode: [TreeNode]) -> Optional[TreeNode]:
        if not root:
            return newnode

        if newnode.val < root.val:
            root.left = self.insertNode(root.left, newnode)
        else:
            root.right = self.insertNode(root.right, newnode)
        
        return root

    def deleteNode0(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node, parent):
            if not node:
                return None

            if node.val == key:

                if node == parent.left:
                    parent.left = None
                else:
                    parent.right = None
                return node

            if key < node.val:
                res = dfs(node.left, node)
            else:
                res = dfs(node.right, node)
            if res: 
                return res

        if not root:
            return TreeNode(key)
    
        if root.val == key:
#            root = None
            delNode = root
            root = None
        else:
            delNode = dfs(root, None)
#        print(f'find {delNode.val}')
#        return root
        res = root

        if delNode:
            left = delNode.left
            right = delNode.right

            if left:
#                print(f'insert {left.val}')
                res = self.insertNode(res, left)
            if right:
#                print(f'insert {right.val}')
                res = self.insertNode(res, right)

        return res

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            #root is deleted
            if not root.left:
                return root.right
            if not root.left:
                return root.right

            # both children exist
            rightmost = root.left
            while rightmost.right:
                rightmost = rightmost.right
            #rightmost in root.left
            rightmost.right = root.right

            return root.left

        return root
