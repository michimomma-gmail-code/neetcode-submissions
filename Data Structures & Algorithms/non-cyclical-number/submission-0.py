class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def compute(n):
            if n in seen:
                return False
            seen.add(n)

            nstr = str(n)
            total = 0
            for dig in nstr:
                total += int(dig) ** 2
            if total == 1:
                return True
            else:
                return compute(total)

        
        return compute(n)