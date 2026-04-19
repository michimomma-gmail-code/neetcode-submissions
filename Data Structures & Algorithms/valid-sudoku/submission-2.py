class Solution:
    def _isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. row check, rowcount for each row
        # 2. col check, colcount for each col
        colcount = defaultdict(dict)
        groupcount = defaultdict(lambda: defaultdict(dict))
        for r in range(9):
            rowcount = {}
            group_r = r // 3
            for c in range(9):

                group_c = c // 3

                print(group_r, group_c)

                num = board[r][c]
                if num == ".":
                    continue
                if num in rowcount:
                    print("row false")
                    print(board[r])
                    return False
                rowcount[num] = 1
    
                if num in colcount[c]:
                    print("col false")
                    return False
                colcount[c][num] = 1

                if num in groupcount[group_r][group_c]:
                    print("group false")
                    return False
                groupcount[group_r][group_c][num] = 1


        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        anycount = defaultdict(dict)

        for r in range(9):
            group_r = r // 3
            for c in range(9):
                group_c = c // 3

                num = board[r][c]
                if num == ".":
                    continue

                if num in anycount[(r,-1)]:
                    return False
                anycount[(r,-1)][num] = 1

                if num in anycount[(-1,c)]:
                    return False
                anycount[(-1,c)][num] = 1
    
                if num in anycount[(group_r, group_c)]:
                    return False
                anycount[(group_r, group_c)][num] = 1


        return True
