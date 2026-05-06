class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [0] * n
        dp[0], dp[1] = 1, 2

        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
        
        print(dp)

        return dp[n-1]