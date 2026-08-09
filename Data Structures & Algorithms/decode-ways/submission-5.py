class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        # dp = [0] * (N + 2)
        dp0, dp1, dp2 = 0, 1, 0
        # dp[N] = 1

        for i in range(N - 1, -1, -1):
            curr_dig = s[i]
            next_dig = s[i + 1] if i + 1 < N else None

            if curr_dig == '0':
                dp2 = dp1
                dp1 = 0
                dp0 = 0
                continue
            
            dp0 += dp1
            if curr_dig in "12":
                if next_dig and int(''.join([curr_dig, next_dig])) <= 26:
                    dp0 += dp2
            dp2 = dp1
            dp1 = dp0
            dp0 = 0

        return dp1