class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node] 
#        print(self.parent)
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False
        else:
            if self.rank[root1] > self.rank[root2]:
                self.rank[root1] += self.rank[root2]
                self.parent[root2] = root1
            else:
                self.rank[root2] += self.rank[root1]
                self.parent[root1] = root2
            return True


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

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        n = len(accounts)
        uf = UnionFind(n)

        email2act = {}
        for i, act in enumerate(accounts):
            for email in act[1:]:
                if email in email2act:
                    nxt_i = email2act[email]
                    uf.union(i, nxt_i)
                else:
                    email2act[email] = i

        p2email = defaultdict(set)
        for i, act in enumerate(accounts):
            p_i = uf.find(i)
            p2email[p_i].update(act[1:])
        
#        res = [[accounts[i][0]] + sorted(list(p2email[i]))] for i in p2email
        res = []
        for i in p2email:
            res.append( [accounts[i][0]] + sorted( p2email[i] ) )

        return res