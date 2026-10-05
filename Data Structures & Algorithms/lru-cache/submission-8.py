# class Node:
#     def __init__(self, key = None, val = None):
#         self.key, self.val = key, val
#         self.prev = self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.head = Node()
#         self.tail = Node()
#         self.head.next, self.tail.prev = self.tail, self.head

#     def _insert(self, node):
#         # head
#         # head <-> head.next
#         # head <-> node <-> head.next (next)
#         next = self.head.next # tail
#         head = self.head
#         self.head.next, node.next = node, next
# #        self.head.next.prev, node.prev = node, head
#         next.prev, node.prev = node, head
#         print(f'insert tail-1 = {self.tail.prev.key}')

#     def _remove(self, node):
#         # node.prev <-> node <-> node.next
#         # node.prev <-> node.next
#         prev = node.prev
#         next = node.next
#         prev.next, next.prev = next, prev

#     def get(self, key: int) -> int:

#         if key in self.cache:
#             # put this key into after head
#             node = self.cache[key]
#             self._remove(node)
#             self._insert(node)

#             return node.val
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:

#         if key in self.cache:
#             node = self.cache[key]
#             node.val = value
#             self.get(key)
#             return
        
#         if len(self.cache) == self.capacity:
#             node = self.tail.prev
#             self._remove(node)
#             self.cache.pop(node.key)        
#         # new
#         node = Node(key, value)
#         self.cache[key] = node
#         self._insert(node)


class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # cache: key -> Node (key, val, prev, next)

    def __init__(self, capacity: int):
        self.cache = {} # key, node
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # remove key from DLL
        # node_prev = node.prev
        # node_next = node.next

        # node_prev.next = node.next
        # node_next.prev = node_prev
        node.prev.next, node.next.prev = node.next, node.prev

    def _push_node(self, node):
        head_next = self.head.next

        node.next = head_next
        self.head.next = node
        node.prev = self.head
        head_next.prev = node

        # self.head.next, node.next = node, self.head.next
        # node.prev = self.head
        # self.head.next.prev = node

    def get(self, key: int) -> int:
        # if key in in self.cache
        #   get value from self.cache (hashmap), and return
        #   remove the key from DLL, and push it to 1st pos (refresh the order)
        # else
        #   return -1
#        print("get: ", self.cache)

        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._push_node(node)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 
        # if key in self.cache
        #   update self.cache[key] = val
        #   run get(key), which will push this key-val to the 1st pos
        # else:
        #   if len(self.cache) > self.capacity:
        #       evict last node in DLL
        #       remove the key-val in self.cache
        #   else:
        #      add to self.cache[key] = val
        #      create DLL node, and push it to the 1st pos

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.get(key)
        else:
            if len(self.cache) >= self.capacity:
                node = self.tail.prev
#                print("remove - ", node.key, node.val)
                self._remove(node)
                self.cache.pop(node.key)

            node = Node(key, value)
            self._push_node(node)
            self.cache[key] = node


#        print("put: ", self.cache)
#        print(self.head.next.key, self.tail.prev.key)
































