# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # [[dum] 0 1 (2) 3 4 5], n = 2
        #  after 1 st while: cur = 2
        #  delayed = dum
        # [dum 0 1 2 [3] <4> 5 (None)], n = 2
        #  after 2nd while: cur = None, delayed = 3, skip = 4 (delayed.next)
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        count = 0

        for _ in range(n + 1):
            cur = cur.next

        delayed = dummy

        while cur:
            cur = cur.next
            delayed = delayed.next
        skip = delayed.next
        delayed.next = skip.next

        return dummy.next

        