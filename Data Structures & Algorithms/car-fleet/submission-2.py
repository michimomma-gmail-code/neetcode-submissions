class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        indices = sorted(range(len(speed)), key=lambda i: position[i], reverse=True)

        speed = [speed[i] for i in indices]        
        position = [position[i] for i in indices]        
        res = 0
        # speed changes (only slower when a car catch up with preceding car)
#        print(speed)
#        print(position)
#        print(position_t)
        stack = []
        for i in range(len(speed)):
            time = (target - position[i]) / speed[i]
            if stack and time > stack[-1]:
                stack.append(time)
            if not stack:
                stack.append(time)

#        print(stack)

        return len(stack)