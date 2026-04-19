class Solution:
    def twoSum_0(self, numbers: List[int], target: int) -> List[int]:
        
        for i1 in range(len(numbers)):
            n1 = numbers[i1]
            seek = target - n1
            if seek < n1:
                return []
            for i2 in range(i1+1, len(numbers)):
#                if i1 == i2: continue 
                n2 = numbers[i2]
                if n2 == seek:
                    print(i1,i2)
                    return [i1+1, i2+1]
        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,2,3,4] target = 3
        # left   right
        # 1+4=5 > 3 -> need to move right (right -1)
        # 1+3=4 > 3
        # 1+2=3 = 3
        # [1,2,3,5] target = 5
        # 1+5 = 6 >5 -> move right (right-1)
        # 1+3 = 4 <5 -> move left (left+1)
        # 2+3 = 5 = 5

        left, right = 0, len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]