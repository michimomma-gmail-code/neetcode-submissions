class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)
                continue

            # ast < 0
            stack.append(ast)

            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                if abs(stack[-1]) == abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                elif abs(stack[-1]) > abs(stack[-2]):
                    temp = stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(temp)
                else:
                    stack.pop()

        return stack
            