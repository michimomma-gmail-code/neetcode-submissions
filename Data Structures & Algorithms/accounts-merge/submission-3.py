class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # adj graph
        # node = i: index in accounts
        # edge: 
        # accounts[i][0] (name) is same
        # accounts[i][1] (email) has at lest one common
        #

        def is_link(i, j):
            if accounts[i][0] != accounts[j][0]:
                return False
            email_i = set(accounts[i][1:])
            email_j = set(accounts[j][1:])
            return len(email_i.intersection(email_j)) > 0

        def merge_node(cc_idx_s):
            name = accounts[cc_idx_s[0]][0]
            emails = set()
            for idx in cc_idx_s: 
                emails.update(accounts[idx][1:])
            emails = list(emails)
            return [name] + sorted(emails)

        n = len(accounts)
        adj = [ [] for _ in range(n) ]
        for i in range(n):
            for j in range(i + 1, n):
                if is_link(i, j):
                    adj[i].append(j)
                    adj[j].append(i)
#        print('adj = ', adj)

        visited = set()

        def dfs(node):
            res = [node]
            visited.add(node)
            for nxt in adj[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    res.extend(dfs(nxt))
            return res

        res = []
        for i in range(n):
            if i in visited:
                continue
            cc_index = dfs(i)
            # if not cc_index:
            #     continue
            merged = merge_node(cc_index)
            res.append(merged)

        return res
