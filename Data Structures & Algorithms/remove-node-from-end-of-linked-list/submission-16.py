# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        total = 0
        while cur:
            temp = cur.next
            cur = temp
            total += 1
        
        print('total = ', total)

        dummy = ListNode()
        dummy.next = head
        cur = head
        i = 0
        prev = dummy
        while cur:
            temp = cur.next
            if i == (total - n):
                prev.next = cur.next
            else:
                prev = cur
            cur = temp
            i += 1

        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        i = 0
        pn = None
        while cur:
            if i == n:
                pn = cur
                break
            i += 1
            cur = cur.next
        
        dummy = ListNode()
        dummy.next = head
        p = head
        cur = pn
        prev = dummy
        while cur:
            prev = p
            cur = cur.next
            p = p.next
#        if p:
        prev.next = p.next
        # else:
        #     prev.next = None

        return dummy.next
