class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # hashmap: email -> account
        # account -> email -> other accounts (graph)
        # dfs with seen to check accounts already processed
        email2act = defaultdict(list)
        for i, act in enumerate(accounts):
            for email in act[1:]:
                email2act[email].append(i)

#        print(email2act)

        seen = set()

        # output all accounts that merge with i
        def dfs(i):
            act = accounts[i]
            name = act[0]
            all_act = [i]
            seen.add(i)
            for email in act[1:]:
                for nxt_i in email2act[email]:
                    nxt_name = accounts[nxt_i][0]
                    if name == nxt_name:
                        if nxt_i not in seen:
                            seen.add(nxt_i)
                            all_act.extend(dfs(nxt_i))

            return all_act

        def merge(act_id_list):
            # output: list, idx0: name, idx1-: email
            name = accounts[act_id_list[0]][0]
            output = set()
            for act_id in act_id_list:
                output.update( (accounts[act_id][1:]) )
            
            return [name] + sorted(output)

#        print(dfs(0), seen)
        res = []
        for i in range(len(accounts)):
            if i not in seen:
                temp = dfs(i)
#                print(merge(temp))
                res.append(merge(temp))

        return res

