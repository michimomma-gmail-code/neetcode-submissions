class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        # get key push the key to the most recent
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # push the key to the most recent (todo)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        # if exist, remove, then insert
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #evict from head
            temp = self.head.next
            self.remove(temp)
            del self.cache[temp.key]       
