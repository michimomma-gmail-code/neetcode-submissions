# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        while queue:
            
            level_node = []
            for i in range(len(queue)):
                node = queue.popleft()
                level_node.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_node)

        return res


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])

        res = []
        while queue:
            res_lev = []
            for i in range(len(queue)):
                node = queue.popleft()
                res_lev.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(res_lev)

        
        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:

            res_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                res_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(res_level)

        return res


























