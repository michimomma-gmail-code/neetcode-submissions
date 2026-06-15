# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3 -> None
        # 0 next: 1 -> None
        # 1 next: 2 -> 0
        # 2 next: 3 -> 1
        # 3 next: None -> 2
        # 3 -> 2 -> 1 -> 0 -> None
        #
        # need prev to store previous node, which will be linked by the curr node
        # 

        if not head:
            return None

        prev = None
        
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

        