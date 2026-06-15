class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 4444
        # 3444, 4344, 4434, 4443
        # 5555
        # 4555, 5455, 5545, 5554
        #
        # delta = [1000, 100, 10, 1]

        # delta = [1000, 100, 10, 1]
        
        # for de in deadends:
        #     de = int(de)
        #     for dx in delta:
        #         if de - dx == int(target):
        #             return -1

        origin = "0000"
        delta = [1000, 100, 10, 1]
#        delta = ["1000", "0100", "0010", "0001"]

        deadends_set = set()
        for de in deadends:
            deadends_set.add(de)

        def generateNew(in_str, visited):
            new_strs = set()
#            for dx in delta:
            for i in range(len(in_str)):
                for j in [-1, 1]:
                    digit = (int(in_str[i]) + j) %10
#                    if digit < 0:
#                        continue
                    new_str = str(in_str[:i] + str(digit) + in_str[i + 1:])
                    if new_str not in visited:
                        new_strs.add(new_str)
            return list(new_strs)

        temp = generateNew("0009", {})
#        print(temp)


#        mindist_heap = [(0, origin)]
        # cur_str = origin ("0000"()
        queue = deque([origin])
        level = 0
        cnt = 0
        visited = set()
        while queue:
            level += 1
#            print(f'queue = {queue}')
            for i in range(len(queue)):
                cur_str = queue.popleft()
                if cur_str == target:
                    return level - 1
                if cur_str in deadends_set:
                    continue
                new_strs = generateNew(cur_str, visited)
                for nstr in new_strs:
                    if nstr not in visited:
                        queue.append(nstr)
                        visited.add(nstr)
                
            cnt += 1
        return -1
