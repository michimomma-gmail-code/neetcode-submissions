class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        res = defaultdict(list)
        for s in strs:
            array = [0] * 26 
            for char in s:
                idx = ord(char) - ord("a")
                array[idx] += 1

#            print(s, array)

            #key = "_".join([ str(i) for i in array])
            res[tuple(array)].append(s)

#        print(res)

        return list(res.values())




    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = defaultdict(list)
        # distribution (array) -> index

        for i in range(len(strs)):
            s = strs[i]
            dist = [0] * 26
            for char in s:
                idx = ord(char) - ord("a")
                dist[idx] += 1
            seen[tuple(dist)].append(s)

        return [l for l in seen.values() ]








































