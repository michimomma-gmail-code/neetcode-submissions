# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1, l2):
            head = ListNode()
            ch = head
            c1, c2 = l1, l2
            while c1 and c2:
                if c1.val < c2.val:
                    ch.next = c1
                    c1 = c1.next
                else:
                    ch.next = c2
                    c2 = c2.next
                ch = ch.next
            ch.next = c1 if c1 else c2

            return head.next

        if lists == []:
            return None
        res = lists[0]
        for i in range(1, len(lists)):
            res = merge2Lists(lists[i], res)

        return res        
        