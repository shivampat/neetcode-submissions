class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = {len(s) - 1:s[len(s) - 1] == '0'}
        def dfs(i):
            nonlocal dp
            if i in dp:
                return dp[i]
            if s[i] == '1':
                return False

            start = i + minJump
            end = min(i + maxJump, len(s) - 1) 
            for j in range(end, start - 1, -1):
                if dfs(j):
                    dp[j] = True
                    return True

            dp[i] = False 
            return False
        
        return dfs(0)