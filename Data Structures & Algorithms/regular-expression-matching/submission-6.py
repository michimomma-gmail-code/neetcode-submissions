class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n  = len(s), len(p)

        dp = [ [False] * (n + 1) for _ in range(m + 1) ]

        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for r in range(1, m + 1):
            for c in range(1, n + 1):

                if s[r - 1] == p[c - 1] or p[c - 1] == ".":
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[c - 1] == "*":
                    prev_char = p[c - 2]
                    zero_use = dp[r][c - 2]

                    multi_use = False
                    if prev_char == "." or prev_char == s[r - 1]:
                        multi_use = dp[r - 1][c]

                    dp[r][c] = zero_use or multi_use

        return dp[m][n]



    def isMatch1(self, s: str, p: str) -> bool:
        n = len(p)
        
        # dp[j] means: Does the current substring of `s` match `p[:j]`?
        dp = [False] * (n + 1)
        
        # Base Case 1: Empty string matches empty pattern
        dp[0] = True
        
        # Base Case 2: Empty string matching patterns like "a*b*"
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 2]
                
        # Outer Loop: Traverse the string `s`
        for i in range(1, len(s) + 1):
            
            # prev_diag holds dp[i-1][j-1]
            # At the start of a new row, the "diagonal" for j=1 is the old dp[0]
            prev_diag = dp[0] 
            
            # A non-empty string can NEVER match an empty pattern
            dp[0] = False 
            
            # Inner Loop: Traverse the pattern `p` (Left to Right!)
            for j in range(1, n + 1):
                
                # Save the current dp[j] BEFORE we overwrite it. 
                # This will become the prev_diag for the NEXT iteration (j + 1)
                temp = dp[j] 
                
                # Case 1: Normal character or '.'
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # We use the saved diagonal value
                    dp[j] = prev_diag
                    
                # Case 2: The '*' character
                elif p[j - 1] == '*':
                    prev_pattern_char = p[j - 2]
                    
                    # Scenario A: Zero uses -> Look 2 spots left (already updated for current 'i')
                    zero_uses = dp[j - 2]
                    
                    # Scenario B: Multiple uses -> Look "up" (which is just the current dp[j] before overwrite)
                    multiple_uses = False
                    if prev_pattern_char == '.' or prev_pattern_char == s[i - 1]:
                        multiple_uses = dp[j] 
                        
                    dp[j] = zero_uses or multiple_uses
                    
                else:
                    dp[j] = False
                
                # Update prev_diag for the next step of the inner loop
                prev_diag = temp 
                
        return dp[n]