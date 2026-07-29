# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        dummy = ListNode()
        dummy.next = head

#        print(gcd(3, 4))
#        cur -> cur.next -> cur.next.next
#.       12 -> 3 -> 4
#        cut -> cur.next -> gcd -> cur.next.next
#        12 -> (GCD 3) -> 3 -> 4 -> 6
#        12 -> (GCD 3) -> 3 -> (GCD 1) -> 4 -> 6
#        12 -> (GCD 3) -> 3 -> (GCD 1) -> 4 -> (GCD 2) -> 6

        cur = dummy.next
        while cur and cur.next:
        #     temp = cur.next
#            nextp = cur.next.next
            cur_next = cur.next
#            print(f"pair = {cur.val} {cur.next.val}")
            gcd_val = gcd(cur.val, cur.next.val)
            gcd_node = ListNode(gcd_val, cur_next)
            cur.next = gcd_node
        #     cur = temp
            cur = cur_next

        return dummy.next
