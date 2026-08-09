class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 2)
        dp[N] = 1

        for i in range(N - 1, -1, -1):
            curr_dig = s[i]
            next_dig = s[i + 1] if i + 1 < N else None

            if curr_dig == '0':
                dp[i] = 0
                continue
            
            dp[i] += dp[i + 1]
            if curr_dig in "12":
                if next_dig and int(''.join([curr_dig, next_dig])) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]