class MyHashSet:

    def __init__(self):
        self.items = [False] * 1000000
        #defaultlist(lambda: False)

    def add(self, key: int) -> None:
        self.items[key] = True
        

    def remove(self, key: int) -> None:
        self.items[key] = False

    def contains(self, key: int) -> bool:
        if len(self.items) > key and self.items[key]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)