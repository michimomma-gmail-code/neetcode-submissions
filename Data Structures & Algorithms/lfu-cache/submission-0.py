class LFUCache:
    # need this:
    # freq -> node
    # also, track least frequency at any time
    # freq[lest frequent] -> node
    # the node can be deleted by node.prev.next and node.next.prev
    # 
    # how to track min freq
    # 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> val
        self.freq = {} # key -> freq
        self.freqToNode = defaultdict(OrderedDict)
        self.minFreq = float("infinity")
        # self.nodeHead = Node()
        # self.nodeTail = Node()
        # self.nodeHead.next, self.nodeTail.prev = self.nodeTail, self.nodeHead

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        current_freq = self.freq[key]

        self.freq[key] += 1

        self.freqToNode[current_freq].pop(key)
        self.freqToNode[current_freq + 1][key] = 1

        if current_freq == self.minFreq and len(self.freqToNode[current_freq]) == 0:
            self.minFreq += 1

        return self.cache[key]

    def updateMinFreq(self):
        currentMin = self.minFreq
        while not currentMin in self.freq:
            currentMin += 1
        self.minFreq = currentMin

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return

        if len(self.cache) >= self.capacity:
#            removeKey = self.freq[self.minFreq]
            removeKey, _ = self.freqToNode[self.minFreq].popitem(last=False)            
            self.cache.pop( removeKey )
            self.freq.pop( removeKey ) # update min freq, and remove the key from DLL

        self.cache[key] = value
        self.freq[key] = 1
        self.freqToNode[1][key] = 1

        self.minFreq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)