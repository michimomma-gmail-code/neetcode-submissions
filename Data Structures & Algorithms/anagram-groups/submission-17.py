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

            key = "_".join([ str(i) for i in array])
            res[key].append(s)

#        print(res)

        return [ res[k] for k in res ]