# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2Lists(self, list1, list2):
        res = node = ListNode()
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                node.next = cur1
                cur1 = cur1.next
            else:
                node.next = cur2
                cur2 = cur2.next
            node = node.next

        node.next = cur1 if cur1 else cur2
        return res.next

    def devide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        mid = l + (r - l) // 2
        left = self.devide(lists, l, mid)
        right = self.devide(lists, mid+1, r)
        return self.merge2Lists(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if lists == []:
            return None
        # res = []
        # for i in range(len(lists)):
        #     res = self.merge2Lists(res, lists[i])
        res = self.devide(lists, 0, len(lists)-1)

        return res
        