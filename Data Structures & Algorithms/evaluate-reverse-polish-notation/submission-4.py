class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ("+","-","*","/"):
                stack.append(int(t))
            else:
                if t == "+":
                    res = stack.pop() + stack.pop()
                elif t == "-":
                    print(stack)
                    res = - (stack.pop() - stack.pop())
                elif t == "*":
                    res = stack.pop() * stack.pop()
                elif t == "/":
                    x1 = stack.pop()
                    x2 = stack.pop()
                    res = int(x2 / x1)
                print(f'res = {res}')
                stack.append(res)

            print(stack)
        return stack[-1]