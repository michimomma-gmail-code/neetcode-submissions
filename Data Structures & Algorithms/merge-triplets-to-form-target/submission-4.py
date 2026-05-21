class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        done = set()
        for t in triplets:

#             is_triplet_good = True
#             for j in range(3):
#                 if triplets[i][j] > target[j]:
#                     is_triplet_good = False
                
#             if not is_triplet_good:
# #                print(f'{i} removed')
#                 continue
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for j in range(3):
                if t[j] == target[j]:
                    done.add(j)

#        print(done)

        return len(done) == 3






        