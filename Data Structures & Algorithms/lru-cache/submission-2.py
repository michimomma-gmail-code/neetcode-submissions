class Node:
    def __init__(self, key = None, val = None):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _insert(self, node):
        # head
        # head <-> head.next
        # head <-> node <-> head.next (next)
        next = self.head.next # tail
        if next == self.tail:
            print("inserting before tail")
        head = self.head
        self.head.next, node.next = node, next
        next.prev, node.prev = node, head
        print(f'insert tail-1 = {self.tail.prev.key}')

    def _remove(self, node):
        # node.prev <-> node <-> node.next
        # node.prev <-> node.next
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
#        print(f'tail-1 = {self.tail.prev.key}')

        if key in self.cache:
            # put this key into after head
            node = self.cache[key]
            print(f'removing {node.key} {node.val}')
            self._remove(node)
            print(f'removed')
            self._insert(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.get(key)
            return
        
        if len(self.cache) == self.capacity:
            node = self.tail.prev
            print(f'removing {node.key} {node.val}')
            self._remove(node)
            print(f'removed')
            self.cache.pop(node.key)        
        # new
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        print(f'tail-1 = {self.tail.prev.key}')


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.head, self.tail = Node(0, 0), Node(0, 0)
#         self.head.next, self.tail.prev = self.tail, self.head

#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev
    
#     def insert(self, node):
#         prev, nxt = self.tail.prev, self.tail
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev

#     def get(self, key: int) -> int:
#         # get key push the key to the most recent
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             # push the key to the most recent (todo)
#             return self.cache[key].val
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:

#         # if exist, remove, then insert
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.capacity:
#             #evict from head
#             temp = self.head.next
#             self.remove(temp)
#             del self.cache[temp.key]       
