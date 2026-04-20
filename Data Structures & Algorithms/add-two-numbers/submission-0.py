# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        newlist = ListNode()
        new_c = newlist
        carry = 0
        while cur1 or cur2:
            val1, val2 = 0, 0
            if cur1:
                val1 = cur1.val
            if cur2:
                val2 = cur2.val 
            sum = val1 + val2 + carry
            carry = 0
            if sum >= 10:
                carry = 1
            new_c.next = ListNode(val = sum % 10)
            cur1 = cur1.next if cur1 is not None else None
            cur2 = cur2.next if cur2 is not None else None
            new_c = new_c.next

        if carry == 1:
            new_c.next = ListNode(val = 1)

        return newlist.next