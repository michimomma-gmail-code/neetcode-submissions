
class Node:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        
class MyCircularQueue:
# 1 -> 2 -> 3 -> 1
#.  <-   <-   <-  

#["MyCircularQueue","enQueue","enQueue","deQueue","enQueue","deQueue","enQueue","deQueue","enQueue","deQueue", "Front"]
#[[2].              ,[1]       ,[2]      ,[]      ,[3]      ,[]      ,[3]      ,[]       ,[3]      ,[]        ,[]]
    def __init__(self, k: int):
        self.max_elems = k
        self.cur_elems = 0
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        # add one to the tail
        if self.cur_elems < self.max_elems:
            node = Node(value)
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node
            self.cur_elems += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        # delete from tail?
        if self.cur_elems == 0:
            return False
        to_delete = self.head.next
        next = to_delete.next
        next.prev = self.head
        self.head.next = next
        self.cur_elems -= 1
        return True


    def Front(self) -> int:
        # peek from head
        return self.head.next.val

    def Rear(self) -> int:
        # peek from tail
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        # check head and tail
        return self.head.next == self.tail and self.tail.prev == self.head

    def isFull(self) -> bool:
        # check number of elements
        return self.cur_elems == self.max_elems


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()