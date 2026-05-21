class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        card_counts = Counter(hand)

        print(card_counts)
        sorted_counts = sorted(card_counts.keys())
        print(sorted_counts)

        for card in sorted_counts:

            this_card_counts = card_counts[card]

            if this_card_counts > 0:

                for i in range(groupSize):
                    if card_counts[ card + i ] < this_card_counts:
                        return False

                    card_counts[ card + i ] -= this_card_counts

        return True