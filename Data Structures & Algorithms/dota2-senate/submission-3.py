class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qR = deque([i for i in range(n) if senate[i] == "R"])
        qD = deque([i for i in range(n) if senate[i] == "D"])

        while qR and qD:
            i_R = qR.popleft()
            i_D = qD.popleft()

            if i_R < i_D:
                # inactivete D, adding i_R back for next round
                qR.append( i_R + n )
            else:
                qD.append( i_D + n )

        if qR:
            return "Radiant"
        else:
            return "Dire"

    def predictPartyVictory(self, senate: str) -> str:
        senators = list(senate)
        r_count = senators.count("R")
        d_count = senators.count("D")

        r_ban = d_ban = 0

        while r_count > 0 and d_count > 0:
            for i in range(len(senators)):
                if senators[i] == "X":
                    continue
                
                if senators[i] == "R":
                    if r_ban > 0:
                        r_ban -= 1
                        senators[i] = "X"
                        r_count -= 1
                    else:
                        d_ban += 1
                elif senators[i] == "D":
                    if d_ban > 0:
                        d_ban -= 1
                        senators[i] = "X"
                        d_count -= 1
                    else:
                        r_ban += 1


        return "Radiant" if r_count > 0 else "Dire"
            
                    
