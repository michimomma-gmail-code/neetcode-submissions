class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.max_elems = k
        self.cur_elems = 0

        self.head_index = 0
        self.tail_index = 0

    def enQueue(self, value: int) -> bool:

        # print(self.queue)
        # print('head = ', self.head_index)
        # print('tail = ', self.tail_index)
        # print('cur elems = ', self.cur_elems)

        if self.isFull():
            return False

        index = self.tail_index % self.max_elems
        self.queue[ index ] = value
        self.tail_index = (self.tail_index + 1) % self.max_elems
        self.cur_elems += 1

        return True
        # after one enque, tail_index = 1,head_index = 0
        # if dequeue, head_index = 1, 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head_index = (self.head_index + 1) % self.max_elems
        self.cur_elems -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.head_index]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # index of tail is tail_index - 1
        index = (self.tail_index - 1) % self.max_elems

        return self.queue[index]

    def isEmpty(self) -> bool:
        return self.cur_elems == 0

    def isFull(self) -> bool:
        return self.cur_elems == self.max_elems
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()