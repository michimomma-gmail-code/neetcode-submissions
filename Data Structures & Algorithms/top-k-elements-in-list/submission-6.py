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
        count = defaultdict(int)
        maxcount = 0
        for num in nums:
            count[num] += 1
            if count[num] > maxcount:
                maxcount = count[num]

        bucket = [[] for i in range(maxcount + 1)]
        print(count)
        print(bucket)
        for num, freq in count.items():
            bucket[freq].append(num)

        print(bucket)
        result = []
        lb = len(bucket)
        for i in range(lb):
            index = lb -1 - i

            for num in bucket[index]:
                result.append(num)
                if len(result) == k:
                    return result
    #        print(result)

