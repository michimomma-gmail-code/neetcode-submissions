class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        for opr in operations:
            if opr == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(int(a) + int(b))
            elif opr == "C":
                stack.pop()
            elif opr == "D":
                a = stack[-1]
                stack.append(int(a) * 2)
            else:
                stack.append(int(opr))
#        print(stack)
        return sum(stack)