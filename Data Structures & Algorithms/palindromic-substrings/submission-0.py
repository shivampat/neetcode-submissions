class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(len(s) - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
        
        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 2, len(s)):
                dp[start][end] = s[start] == s[end] and dp[start + 1][end - 1]
        
        numSubstrings = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j]:
                    numSubstrings += 1
        
        return numSubstrings
