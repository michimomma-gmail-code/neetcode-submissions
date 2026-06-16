# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

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
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #
        # pull and keep k-heads (at last one from each list) in minheap
        # always pull min from k-heads.
        # to keep minimal list, track (val, list-index), once it is popped, pull from the list
        #
        minheap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minheap, (lists[i].val, i) )
#                lists[i] = lists[i].next

        print(minheap)
        head = ListNode(-1)
        curr = head
        while minheap:
            minval, list_index = heapq.heappop(minheap)
            print('minval = ', minval, 'index = ', list_index, 'cur_val = ', curr.val)
            curr.next = lists[list_index]
            curr = curr.next
#            curr = curr.next
            lists[list_index] = lists[list_index].next

#            push from list_index
            if lists[list_index]:
                heapq.heappush(minheap, (lists[list_index].val, list_index))


        return head.next



