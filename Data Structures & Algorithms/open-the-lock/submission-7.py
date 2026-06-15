class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:


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
                        visited.add(new_str)

            return list(new_strs)

#        temp = generateNew("0009", {})
#        print(temp)


#        mindist_heap = [(0, origin)]
        # cur_str = origin ("0000"()
        visited = set(deadends)
        origin = "0000"
        if origin in visited:
            return -1
        visited.add(origin)
        queue = deque([origin])
        level = 0
        cnt = 0
        while queue:
#            print(f'queue = {queue}')
            for _ in range(len(queue)):
                cur_str = queue.popleft()
                if cur_str == target:
                    return level 
                # if cur_str in visited:
                #     continue
                new_strs = generateNew(cur_str, visited)
                for nstr in new_strs:
                    queue.append(nstr)
                #     if nstr not in visited:
                #         queue.append(nstr)
                #         visited.add(nstr)
                
            level += 1
        return -1
