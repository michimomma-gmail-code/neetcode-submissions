class Solution:
    def isHappy0(self, n: int) -> bool:
        
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

    def isHappy(self, n: int) -> bool:

        def compute(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10            
            return total
        
        slow = n
        fast = compute(n)

        while fast != 1 and slow != fast:
            slow = compute(slow)
            fast = compute(compute(fast))

        return fast == 1
                
