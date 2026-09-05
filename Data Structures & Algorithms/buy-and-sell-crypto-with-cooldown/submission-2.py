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
            hold = max( hold, empty_ready - p)
            empty_ready = max( empty_cooldown, empty_ready )
            empty_cooldown = p + hold

        return max(empty_ready, empty_cooldown)


        #
        # state (end of day)
        #   hold (ready to sell) 
        #   coold down (sold / cool down)
        #   free (no coin)
        # state transition
        #   hold (ready to sell) -> hold (ready to sell)
        #   cool down -> hold 
        #   sell (sold / cool down) -> cooldown 

        #   free -> hold
        #   free -> feee (nothing)

        # free = 0
        # sell = - float("inf")
        # hold = - float("inf")

        # for p in prices:
        #     free = max(free, p + hold)
        #     hold = max(hold, free - p)

        # return free