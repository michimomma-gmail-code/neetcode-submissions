class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 
        people.sort()
        print(people)
        count = 0 

        target = limit

        left, right = 0, len(people) - 1
        # [1, 1, 1, 1, 2, 2, 3, 3], limit = 3
        # 

        while left <= right:
            
            current = people[left] + people[right]
            if current <= target:
                left += 1
            
            right -= 1
            count += 1

#        print(index_pairs)
        return count
            
