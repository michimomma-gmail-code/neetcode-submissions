class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # node1 -> node2
        #       -> node3
        in_deg = {}
        out_deg = {}
        for n1, n2 in trust:
            in_deg[n2] = 1 + in_deg.get(n2, 0)
            out_deg[n1] = 1 + out_deg.get(n1, 0)

        for i in range(1, n + 1):
            if i in out_deg:
                continue
            if i in in_deg and in_deg[i] == (n - 1):
                return i

        return -1