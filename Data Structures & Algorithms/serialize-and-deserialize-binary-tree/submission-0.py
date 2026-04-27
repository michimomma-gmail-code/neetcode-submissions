# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
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
    def deserialize(self, data: str) -> Optional[TreeNode]:
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
            else:
                node.left = None
            if indata[index] != "N":
                queue.append(node.left)

            index += 1
            if indata[index] != "N":
                node.right = TreeNode(indata[index])
            else:
                node.right = None

            if indata[index] != "N":
                queue.append(node.right)

        return root
