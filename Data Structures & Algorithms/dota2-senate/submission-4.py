class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        senates = list(senate)

        qD = deque([i for i in range(n) if senates[i] == "D"])
        qR = deque([i for i in range(n) if senates[i] == "R"])

        while qD and qR:

            idx_d = qD.popleft()
            idx_r = qR.popleft()

            if idx_d < idx_r:
                qD.append(idx_d + n)

            else:
                qR.append(idx_r + n)

        return "Radiant" if qR else "Dire"