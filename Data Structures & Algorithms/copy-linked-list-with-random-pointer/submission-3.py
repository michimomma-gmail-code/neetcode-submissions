"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
 #       listarray = []
        ref2index = {}
        randomnoderef = []
        
        newlistarray = []
        index = 0
        while cur:
            ref2index[cur] = index #random node ref
            newlistarray.append(Node(x = cur.val))
            randomnoderef.append(cur.random)
            cur = cur.next
            index += 1
        print(ref2index)
        print(randomnoderef)

        randomnodeindex = [None] * len(randomnoderef)

        for index, rnr in enumerate(randomnoderef):
            if rnr in ref2index:
                rnindex = ref2index[rnr]
                randomnodeindex[index] = rnindex

        print(randomnodeindex)
        print(newlistarray)
        newlistarray.append(None)
        res = None
        for index in range(len(newlistarray)-1):
            newnode = newlistarray[index]
            print(f'newnode val = {newnode.val}')
            newnode.next = newlistarray[index + 1]
            print(randomnodeindex[index])
            if randomnodeindex[index] is None:
                newnode.random = None
            else:
                newnode.random = newlistarray[randomnodeindex[index]]
            if index == 0:
                res = newnode

        # cur index -> random node ref -> index of random node
        return res