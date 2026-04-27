# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize0(self, root: Optional[TreeNode]) -> str:
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")

        res = ",".join(res)        
        print(f'res = {res}')
        
        return(res)

        
    # Decodes your encoded data to tree.
    def deserialize0(self, data: str) -> Optional[TreeNode]:
        if data == "N":
            return None
        indata = data.split(",")
#        print(f'indata = {indata}')

        root = TreeNode(indata[0])
        queue = deque([root])
        index = 0
        while queue:
            index += 1
            node = queue.popleft()
#            print(f'index = {index}, node = {node.val}')
            if indata[index] != "N":
                node.left = TreeNode(indata[index])
                queue.append(node.left)

            index += 1
            if indata[index] != "N":
                node.right = TreeNode(indata[index])
                queue.append(node.right)

        return root


    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def dfs(node):
            if not node:
                self.res.append("N")
                return

            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        print(self.res)

        return ",".join(self.res)

    def _deserialize(self, data: str) -> Optional[TreeNode]:

        if data == "N":
            return None

        data = data.split(",")

        index = 0

        def dfs(node):
            nonlocal index 

            if not node:
                return
            
            index += 1
            if data[index] != "N":
                node.left = TreeNode(data[index])                
            dfs(node.left)

            index += 1
            if data[index] != "N":
                node.right = TreeNode(data[index])
            dfs(node.right)


        root = TreeNode(data[0])
        dfs(root)


        return root

    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data == "N":
            return None
            
        data = data.split(",")

        index = 0

        def dfs():
            nonlocal index 
            

            if data[index] == "N":
                index += 1
                return None

            node = TreeNode(data[index])

            index += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

