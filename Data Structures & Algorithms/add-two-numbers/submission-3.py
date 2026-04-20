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
        while cur1 or cur2 or carry:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            new_c.next = ListNode(val = total % 10)

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            new_c = new_c.next

        return newlist.next