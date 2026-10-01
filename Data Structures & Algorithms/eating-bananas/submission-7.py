class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def verify(piles, h, k):
            tot = 0
            for p in piles:
                tot += - (-p // k)
            print(f'tot = {tot}')
            if tot <= h:
                return True
            else:
                return False
        
        m = 0
        for p in piles:
            m = max(p, m)

        l, u = 0, m
        min_k = m
        while l <= u and u > 0:
            mid = - (-(l + u) // 2)
            tmp = verify(piles, h, mid)
#            print(f'mid = {mid}, verify = {tmp}')
            if tmp:
                min_k = min(min_k, mid)
                u = mid -1
            else:
                l = mid +1
        return min_k

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def is_valid(k):
            total = 0
            for p in piles:
                total += - ( (- p) // k )
            return total <= h

        l, r = max(1, min(piles)//h), max(piles)

        while l < r:
            mid = (l + r) // 2

            if is_valid(mid):
                r = mid
            else:
                l = mid + 1

        return l
        


















