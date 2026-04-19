# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        cur = head
        slow = head
#        count = 0
        while cur and cur.next:
            slow = slow.next
            cur = cur.next.next
#            count += 1

            if slow == cur:
                return True

        return False