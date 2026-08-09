class Solution:
    def numDecodings(self, s: str) -> int:
        # if digit is 1, we have two options:
        # - continue with 'A' and go next
        # - continue with 1 + next digit letter
        # if we can reach the end with these one letter two letter combos, add 1 to # of ways
        # if digit is 2, we have two specific options:
        # - continue with 'B' and go next
        # - continue with 1 + next digit if next digit <= 6, otherwise we dont continue
        # if digit is 0, we can't continue since 0 cannot be a leading digit
        N = len(s)
        dp = {N:1}

        def dfs(i):
            nonlocal N
            if i in dp:
                return dp[i]
            if s[i] == '0':
                dp[i] = 0
                return dp[i]

            if s[i] == '1':
                # continue with just A
                total = 0
                if i + 1 < N:
                    total += dfs(i + 2)
                total += dfs(i + 1)
                dp[i] = total
                return dp[i]
            if s[i] == '2':
                total = 0
                if i + 1 < N and int(s[i + 1]) <= 6:
                    total += dfs(i + 2)
                total += dfs(i + 1)
                dp[i] = total
                return dp[i]
            dp[i] = dfs(i + 1)
            return dp[i]

        dfs(0)        
        return dp[0]