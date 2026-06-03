class FreqStack:

# stack
# 5 -> mf = 5. push. stack = [(5, 1)]
# 7 -> mf = 5, 7. push. stack = [(5, 1) (7, 1)]
# 5 -> mf = 5. pop (7,1)    stack = [(5, 2)], stack2 = [(7,1)]
# 7 -> mf = 5, 7. push. stack = [(5, 2), (7, 2)], stack2 = []
# 4 -> mf = 5, 7. push. stack = [(5, 2), (7, 2)], stack2 = [(4,1)]
# 5 -> mf = 5, pop (til freq == 3) stack = [(5, 3)], stack2 = [(4,1), (7,2)]
# or
# [(5,1) (7,1) (5,2) (7,2) (5,3)]
# "pop" -> 
    def __init__(self):
        self.max_freq = 0
        self.freq_table = {}
        self.freq_stack = defaultdict(list)

    def push(self, val: int) -> None:
        self.freq_table[val] = 1 + self.freq_table.get(val, 0)
        self.freq_stack[ self.freq_table[val] ].append( val )
        self.max_freq = max( self.freq_table[val], self.max_freq )

    def pop(self) -> int:
        res = self.freq_stack[ self.max_freq ].pop()
        self.freq_table[res] -= 1
        if not self.freq_stack[ self.max_freq ]:
            self.max_freq -= 1

        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()