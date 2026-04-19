class Solution:
    def topKFrequent_bf(self, nums: List[int], k: int) -> List[int]:
        # frist, count the frequency
        count = defaultdict(int)
        for v in nums:
            count[v] += 1

        sortedTuple = sorted(count.items(), key=lambda item: item[1], reverse=True)
        result = [sortedTuple[i][0] for i in range(k)]

#        print(result)

        return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frist, count the frequency
        count = {}

        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, freq in count.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

