class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

# Input: target = 10, position = [1,4], speed = [3,2]
# 4 -> 10: time = (10 - 4) / 2 = 3
# 1 -> 10: time = (10 - 1) / 3 = 3
# ans = 1
# 
# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
# 7 -> 10: time = (10 - 7) / 1 = 3 
# 4 -> 10: time = (10 - 4) / 2 = 3
# 1 -> 10: time = (10 - 1) / 2 = 4.5 
# 0 -> 10: time = (10 - 0) / 1 = 10
# ans = 3
        index_sorted = sorted(range(len(position)), key = lambda i: position[i], reverse = True)
        
        position_sorted = [position[i] for i in index_sorted]
        speed_sorted = [speed[i] for i in index_sorted]
        print(position_sorted)
        print(speed_sorted)        

        stack = []
        for i in range(len(position_sorted)):
            survive = True
            time = ( target - position_sorted[i] ) / speed_sorted[i]
#            print(f'time = {time}')
#            count = 0
            if stack and stack[-1] >= time:
#                count += 1
                #a = stack.pop()
                survive = False
#                stack.append(a)

            if survive:
                stack.append(time)
#            print(stack)

        return len(stack)           
