class Solution:
    def partitionLabels1(self, s: str) -> List[int]:
        
        letterCount = Counter(list(s))

#        print(letterCount)

        n = len(s)

        res = []
        currentSet = set()
        currentStart = 0
        for i in range(0, len(s)):
            # for substring so far s[0:i]
            # if count of all letters are 0, split (put in the res)
            # if not, decrement count for s[i]
            #
            letterCount[s[i]] -= 1
            currentSet.add(s[i])

            sub_finish = True
            for char in currentSet:
                if letterCount[char] > 0:
                    sub_finish = False
                    break
            if sub_finish:
                res.append(i - currentStart + 1)
                currentStart = i + 1
                currentSet = set()
        
#        if currentStart <= n - 1:
#            res.append(n - currentStart)

#        print(letterCount)

        return res

    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {char: i for i, char in enumerate(s)}

        res = []
        end = 0
        st = 0

        for i in range(len(s)):
            char = s[i]
            end = max(end, last_occurence[char])

            if i == end: 
                res.append(end - st + 1)
                st = i + 1

        return res