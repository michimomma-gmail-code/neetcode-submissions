class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        letterCount = Counter(list(s))

        print(letterCount)

        n = len(s)

        res = []
        currentSet = set()
        currentSet.add(s[0])
        letterCount[s[0]] -= 1
        currentStart = 0
        for i in range(1, len(s)):
            # for substring so far s[0:i]
            # if count of all letters are 0, split (put in the res)
            # if not, decrement count for s[i]
            #
            sub_finish = True
            for char in currentSet:
                if letterCount[char] > 0:
                    sub_finish = False
                    break
            if sub_finish:
                res.append(i - currentStart)
                currentStart = i
                currentSet = set()
            letterCount[s[i]] -= 1
            currentSet.add(s[i])
        
        if currentStart <= n - 1:
            res.append(n - currentStart)

        print(letterCount)

        return res