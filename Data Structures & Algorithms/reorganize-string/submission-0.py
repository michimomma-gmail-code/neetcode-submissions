class Solution:
    def reorganizeString(self, s: str) -> str:
        # axyy
        # axy y -> yaxy
        # abbccdd
        # abcd bcd -> bacbdcd
        #
        # cccd -> cd cc -> ""
        # abc abc
        # cbabac
        # abcabc

        n = len(s)
        count_s = Counter(s)
        max_heap = [ (-v, k) for k, v in count_s.items() ]
        heapq.heapify( max_heap )

        prev_k = None
        prev_nv = 0
        res = []
        i = 0
        while i < n:

            if not max_heap:
                return ""

            nv, k = heapq.heappop(max_heap)
            res.append(k)
            i += 1

            if prev_k and prev_nv < 0:
                print(f'pushing {prev_k}')
                heapq.heappush(max_heap, (prev_nv, prev_k) )

            prev_k = k
            prev_nv = nv + 1


        print(f'res = {res}')

        return "".join(res)
