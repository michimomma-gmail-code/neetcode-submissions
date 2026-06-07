# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseOne(self, head):
        cur = head 
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev 
            prev = cur
            cur = temp
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #
        dummy = ListNode()
        dummy.next = head

        #
        cur = dummy.next
        n = 0
        while cur:
            cur = cur.next
            n += 1
        n_itr = n // k
        #  dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        #  i % k:   1 -> 2 -> 0 -> 1 -> 1 -> 2 -> 3
        #  dummy -> 3 -> 2 -> 1 -> 4 -> 5 -> 6 -> 

        # reverse 1 -> 2 -> 3 (n) => 3 -> 2 -> 1
        # need to connect
        # prev = dummy
        # top (1) = prev.next
        #     top (1) -> n.next (4)
        #     prev (dummy) -> n (3)

        # reversing 1 -> k

        prev = dummy # 0
        for itr in range(n_itr):
            top = prev.next #1
            cur = prev.next # 1
            old = prev # 0
            for i in range(k): # k = 1 -> 2, k = 3 -> 4
                temp = cur.next # 2
                cur.next = old # 1 -> 0
                old = cur # old = 1 
                cur = temp # cur = 2
            # i = k, cur = k + 1, old = k
            prev.next = old
            top.next = cur
            # iteration
            prev = top


        return dummy.next


