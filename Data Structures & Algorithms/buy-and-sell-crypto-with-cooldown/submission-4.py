class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #
        # empty_ready -> (buy) -> hold 
        # empty_cooldown -> (nothing) -> empty_ready
        # empty_ready -> (nothing) -> empty_ready
        #
        #
        # hold -> (nothing) -> hold
        # hold -> (sell) -> empty (cool down)
        # 

        empty_ready = 0
        empty_cooldown = - float("inf")
        hold = - float("inf")

        for p in prices:
            _hold = hold
            _empty_ready = empty_ready
            hold = max( hold, empty_ready - p)
            empty_ready = max( empty_cooldown, _empty_ready )
            empty_cooldown = p + _hold

        return max(empty_ready, empty_cooldown)

