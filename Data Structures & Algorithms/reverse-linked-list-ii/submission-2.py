# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def printLL(head):
            cur = head
            while cur:
                print(cur.val)
                cur = cur.next

#        printLL(head)

        # cur = head
        # prev = None
        # while cur:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        #printLL(prev)

        cur = head
        index = 0
        left_node = right_node = None
        while cur:
            index += 1
            temp = cur.next
            if index == (left - 1):
                left_node = cur
            if index == (right + 1):
                right_node = cur
                break
            cur = temp

        if not left_node:
            cur = head
        else:
            cur = left_node.next

        prev = right_node

        while cur:
            if cur == right_node:
                break
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        if left_node:
            left_node.next = prev
            return head
        else:
            return prev
