# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        mem = {}
        def dfs(node):
            if not node:
                return 0
            if node in mem:
                return mem[node]

            prevtotal = dfs(node.left) + dfs(node.right)
            prevprevtotal = 0
            if node.left:
                prevprevtotal += dfs(node.left.left) + dfs(node.left.right) 
            if node.right:
                prevprevtotal += dfs(node.right.left) + dfs(node.right.right)

            res = max(prevtotal, prevprevtotal + node.val)
            mem[node] = res
            return res 

        return dfs(root)

        # dp[i]: max amount at i - step
        # dp[i] = max( dp[i - 1], dp[i - 2] + val[i])
        # dp[node] = max(dp[prev], dp[prev.prev] + val[node])
        # dp[node] = max(dp[left] + dp[right], dp[left.lr] + dp[right.lr] + val[node])

