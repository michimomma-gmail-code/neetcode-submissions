class Solution:
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

        while fast != 1 and fast != slow:
            slow = compute(slow)
            fast = compute(compute(fast))

        return fast == 1
