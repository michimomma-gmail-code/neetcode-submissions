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

    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        senates = list(senate)

        r_count, d_count = senates.count("R"), senates.count("D")
        r_ban, d_ban = 0, 0

        while r_count > 0 and d_count > 0:

            for i, sen in enumerate(senates):
                if sen == "X":
                    continue

                if sen == "D":
                    if d_ban > 0:
                        d_ban -= 1
                        d_count -= 1
                        senates[i] = "X"
                    else:
                        r_ban += 1

                else:
                    if r_ban > 0:
                        r_ban -= 1
                        r_count -= 1
                        senates[i] = "X"
                    else:
                        d_ban += 1

        return "Radiant" if r_count > 0 else "Dire"

