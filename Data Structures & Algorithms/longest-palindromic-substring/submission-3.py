class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]  # rows = start i of substr, col = end i of substr
        maxLen = 0
        maxStart = maxEnd = 0

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]

        for start in range(n - 1, -1, -1):
            for end in range(start, n):
                # check if substr in the middle of start,end substr is palin
                # which means we have to check dp[start + 1][end - 1]
                if s[start] == s[end]:
                    if end - start + 1 > 2:
                       dp[start][end] = dp[start + 1][end - 1] 

                if dp[start][end]:
                    if end - start + 1 > maxLen:
                        maxLen = end - start + 1
                        maxStart = start
                        maxEnd = end
        return s[maxStart:maxEnd + 1] 
