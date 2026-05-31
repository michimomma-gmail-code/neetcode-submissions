class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 
        people.sort()
        print(people)
        index_pairs = set()
        selected = set()
        count = 0 

        target = limit

        left, right = 0, len(people) - 1
        # [1, 1, 1, 1, 2, 2, 3, 3], limit = 3
        # 

        while left <= right:
            while left <= right and people[right] > target:
                    right -= 1
            
            while left <= right and (people[right] == target):
                    index_pairs.add( (right) )
                    right -= 1
                    count += 1
            if left > right:
                break
            current = people[left] + people[right]
            if current <= target:
                # found opt pair
                index_pairs.add( (left, right) )
                right -= 1
                left += 1
                count += 1
            else:
                index_pairs.add( (right))
                count += 1
                right -= 1

#        print(index_pairs)
        return count
            
