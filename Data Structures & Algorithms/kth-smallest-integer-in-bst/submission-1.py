# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest0(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        def dfs(node):
            nonlocal cnt
            if not node:
                return 0

            res = 0
            if node.left:
                left = dfs(node.left) + 1
                res += left
                cnt += res
                if cnt == k:
                    return node.left.val
#                    return node.left.val
            if node.right:
                right = dfs(node.right) + 1
                res += right
                cnt += res
                if cnt == k:
                    return node.left.val
#                if right >= k:
#                    return node.right.val
            total = res 
            cnt += 1
            if cnt == k:
                return node.val
 #           if total >= k:
            return node.val 

        return dfs(root) 

    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
#            arr.append(node.val)

        dfs(root)
#        print(arr)
        return arr[k-1]

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            if not node or cnt >= k:
                return
            dfs(node.left)
            cnt += 1
            if cnt == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)

        return res

    