# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList0(self, head: Optional[ListNode]) -> None:
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

    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow = head.next, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
#            print(f'slow in the loop = {slow.val}')
#            print(f'fast in the loop = {fast.val}')

        part2 = slow.next

        slow.next = None

        cur = part2
        while cur:
            print(f'part2: {cur.val}')
            cur = cur.next

        part1 = head
        cur = part1
        while cur:
            print(f'part1: {cur.val}')
            cur = cur.next


#        part2 = slow

        # reverse slow
        cur = part2
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

        cur = part1
        while cur:
            print(f'part1 = {cur.val}')
            cur = cur.next
        
    def reorderList(self, head: Optional[ListNode]) -> None:

        def printlist(head):
            cur = head
            while cur:
                print(cur.val)
                cur = cur.next
        

        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        
        print(n)
        
        n2 = n // 2
        n1 = n - n2
        print(n1, n2)

        l1 = head
        cur = head
        i = 0
        while cur:
            temp = cur.next
            i += 1
            if i == n1:
                cur.next, l2 = None, cur.next
                break
            cur = temp

        print("l1")
        printlist(l1)
        # cur = l1
        # while cur:
        #     print(cur.val)
        #     cur = cur.next

        print("l2")
        printlist(l2)
        # cur = l2
        # while cur:
        #     print(cur.val)
        #     cur = cur.next

        cur = l2
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        l2 = prev

        print("reverse l2")
        printlist(l2)
        # cur = l2
        # while cur:
        #     print(cur.val)
        #     cur = cur.next


        # merge

        c1, c2 = l1, l2
        while c1 and c2:
            p1 = c1.next
            p2 = c2.next
            c1.next, c2.next = c2, c1.next
            c1 = p1
            c2 = p2
        # if c1:
        #     c1.next = None
        # if c2:
        #     c2.next = None

        print("merged: l1")
        printlist(l1)
        # cur = l1
        # while cur:
        #     print(cur.val)
        #     cur = cur.next
        
        head = l1
#        return l1
















