# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, endnode):
        cur = head
        prev = endnode
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
#        prev.next = endnode
        return prev

    def printList(self, head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0
        _head = head
        res = ListNode()
        res.next = head
        prevnode = res
        while cur:
            count += 1
            temp = cur.next
            if count % k == 0:
                
                print(f'k-th node: {cur.val}')
                # reverse, and join
                # save the end node (next)
                endnode_next = cur.next
                cur.next = None

#                self.printList(head)

                rev = self.reverse(_head, endnode_next)
                prevnode.next = rev
                self.printList(rev)

#                cur.next = endnode_next
                prevnode = _head
                _head = endnode_next

            cur = temp

        return res.next
