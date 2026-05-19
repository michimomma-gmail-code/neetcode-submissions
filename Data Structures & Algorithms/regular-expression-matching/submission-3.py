class Solution:
    def isMatch0(self, s: str, p: str) -> bool:
        
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        n2 = len(p)

        # s = "nnn"
        # p = "n*"
        # n = 3
        #
        # j = 1, char = "n"
        # i = 3
        # s[i - 1] = s[2] = "n" == char (n), dp[i = 3] = dp[i - j = 3 - 1 = 2] = F
        # i = 2
        # i - j = 2 - 1 = 1, s[2 - 1] = s[1] = "n" == char, dp[i = 2] = dp[i - j] = dp[2 - 1] = dp[1] = F
        # i = 1
        # i - j = 1 - 1 = 0, s[1 - 1] = s[0] = "n" == char, dp[i = 1] = dp[i - j] = dp[0] = T
        #
        # dp[0] = T, dp[1] = T, dp[2] = F

        # j = 2, char = "*"
        # i = 3
        # s[3 - 1] = s[2] = n != char
        # i - j = 3 - 2 >= 0, dp[i - (j - 1)] = dp[3 - (2 - 1)] = dp[2] = F
        # i = 2
        # i - j = 2 - 2 >= 0, dp[2] = dp[i - (j - 1)] = dp[2 - (2 - 1)] = dp[1] = T

        for j in range(1, len(p) + 1):
            char = p[j - 1]
            for i in range(n, 0, -1): # s
                if i - j >= 0 and (s[i - 1] == char or char == "."):
                    dp[i] = dp[i - j]
                if i - j >= 0 and char == "*":
                    # get length of match, based on "*"
                    dp[i] = dp[i - (len_match)]

        return dp[n]

    def isMatch(self, s: str, p: str) -> bool:
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