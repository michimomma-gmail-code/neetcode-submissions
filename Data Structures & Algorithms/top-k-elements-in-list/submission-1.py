class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frist, count the frequency
        count = defaultdict(int)
        for v in nums:
            count[v] += 1

        sortedTuple = sorted(count.items(), key=lambda item: item[1], reverse=True)
        result = [sortedTuple[i][0] for i in range(k)]

        print(result)

        return result