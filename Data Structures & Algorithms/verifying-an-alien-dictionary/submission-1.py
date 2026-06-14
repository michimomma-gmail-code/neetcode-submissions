class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order2num = {}
        for i, char in enumerate(order):
            order2num[char] = i
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
#            print(w1, w2)
            # if same when one word is exhansted
            # shorter word is earlier
            for j in range(len(w1)):
                if j >= len(w2):
                    return False

                if w1[j] == w2[j]:
                    continue
#                print(f'{w1[j]}: {order2num[w1[j]]}, {w2[j]}: {order2num[w2[j]]}')
                if order2num[w1[j]] < order2num[w2[j]]:
                    break
                else:
                    return False
            
        return True