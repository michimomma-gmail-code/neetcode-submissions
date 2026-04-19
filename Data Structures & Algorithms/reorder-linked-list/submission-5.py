# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head.next
        slow = head
        # [2 (4) 6 8]
        # 0. slow: 2, fast: 4
        # 1. end state slow: 4, fast: 8 (fast.next None)-> break

        # [2 4 (6) 8 10]
        # 0. slow: 2, fast: 4
        # 1. end state slow: 4, fast: 8
        # 2. end state slow: 6, fast: None -> break
        # slow = slow.next
        # [2 4 (6) 8]
        # [2 4 6 (8) 10]

        def printList(head):
            cur = head
            while cur:
#                print(f'value = {cur.val}')
                cur = cur.next
            

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        part2_head = slow.next
        slow.next = None
        part1_head = head

#        print('part1')
#        printList(part1_head)
#        print('part2')
#        printList(part2_head)

        #reverse
        cur = part2_head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        rev = prev
#        print('rev')
#        printList(rev)

        cur = part1_head
        cur_r = rev
        while cur_r:
            temp = cur.next
            temp2 = cur_r.next

            cur.next, cur_r.next = cur_r, cur.next

            cur = temp
            cur_r = temp2
#        print('final')
#        printList(part1_head)
        head = part1_head
        