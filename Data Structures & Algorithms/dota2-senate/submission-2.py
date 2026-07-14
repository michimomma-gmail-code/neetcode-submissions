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