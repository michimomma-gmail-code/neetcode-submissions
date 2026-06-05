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

        if not head:
            return None

        old2new = {}

        cur = head
        while cur:
            temp = cur.next
            old2new[cur] = Node(cur.val)
            cur = temp

        for old in old2new:
            old2new[old].next = old2new.get(old.next, None)
            old2new[old].random = old2new.get(old.random, None)

        return old2new[head]