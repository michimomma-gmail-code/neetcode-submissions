class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # ['',   'neetcode', 'practice', '',     '...', '',     '',    '..', 'courses']
        # ignore, push,       push,      ignore,  push, ignore, ignore, pop, push 
        # ['neetcode', 'practice', '...'] -> pop
        # ['neetcode', 'practice'] -> push
        # ['neetcode', 'practice', 'courses']
        # 

        stack = []

        path_list = path.split("/")

        for s in path_list:
            if not s or s == ".":
                continue
            
            if s == "..":
                if stack: 
                    stack.pop()
                continue
            
            stack.append(s)

        return "/" + "/".join(stack)
