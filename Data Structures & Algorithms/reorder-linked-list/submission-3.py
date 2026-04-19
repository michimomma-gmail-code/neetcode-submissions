# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #        [0 1 2 3 4 5 6]
        # next   [1 2 3 4 5 6]
        # change [0 6 1 5 2 4 3]
        # next   [6 1 5 2 4 3]
        #        [[0] <n-1 = 6> [1] <n-2 = 5> [2] <n-3 = 4> [3]]

        # from orig
        # head -> 0 -> 1 -> 2 -> 3 (7 - 7//2 = 7 - 3 = 4)
        # create new one
        # 4 <- 5 <- 6 <- head2 (7 // 2 = 3)
        # then merge


        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        print(f'length={length}')

        cur = head
        for _ in range( - (-length // 2)):
            prev = cur
            cur = cur.next
        prev.next = None

        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        


        rev = prev
        cur = rev
        while cur:
            print(f'rev = {cur.val}')
            cur = cur.next
        

        cur = head
        while cur and rev:
            temp = cur.next
            temp2 = rev.next
            cur.next = rev
            rev.next = temp
            cur = temp
            rev = temp2     

        cur = head
        while cur:
 #           print(f'final value = {cur.val}')
            cur = cur.next

