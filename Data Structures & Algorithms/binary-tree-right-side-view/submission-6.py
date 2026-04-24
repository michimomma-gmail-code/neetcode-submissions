# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])

        res = []
        while queue:
            rightval = None
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                queue.append(node.left)
                queue.append(node.right)
                rightval = node.val
            if rightval:
                res.append(rightval)

        return res