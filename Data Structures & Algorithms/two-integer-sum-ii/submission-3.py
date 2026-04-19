class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i1 in range(len(numbers)):
            n1 = numbers[i1]
            seek = target - n1
            for i2 in range(i1+1, len(numbers)):
#                if i1 == i2: continue 
                n2 = numbers[i2]
                if n2 == seek:
                    print(i1,i2)
                    return [i1+1, i2+1]
        return []