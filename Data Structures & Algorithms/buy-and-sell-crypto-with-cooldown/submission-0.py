class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: (at the of day)
        # held (have stock)
        # rest (no stock -- no cool down -- free to buy next day)
        # sold (sold stock -- no stock, cool down next day)
        # rest -> buy -> held -> sold -> rest
        # 
        # t = 0
        # rest = 0, sold = -inf, held = -p[0]
        # t = 1
        # held = max(held from t = 0, rest[0] and buy t = 1); max( held[0],  rest[0] - p[1])
        # rest = max(rest from t=0, sold from t = 0); max(rest[0], sold[0])
        # sold = (held t = 0, sold t = 1); hold[0] + p[1]
        # 
        n = len(prices)
        held = [0] * n
        rest = [0] * n
        sold = [0] * n

        held[0] = -prices[0]
        sold[0] = -float("infinity")
        rest[0] = 0

        for i in range(1, n):
            held[i] = max(held[i - 1], rest[i - 1] - prices[i])
            rest[i] = max(rest[i - 1], sold[i - 1])
            sold[i] = held[i - 1] + prices[i]

        return max(sold[n - 1], rest[n - 1])
