class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        done = set()
        for i in range(len(triplets)):

            is_triplet_good = True
            for j in range(3):
                if triplets[i][j] > target[j]:
                    is_triplet_good = False
                
            if not is_triplet_good:
#                print(f'{i} removed')
                continue

            for j in range(3):
                if triplets[i][j] == target[j]:
                    done.add(j)

#        print(done)

        return len(done) == 3






        