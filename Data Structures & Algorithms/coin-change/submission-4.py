class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for curr_amt in range(amount + 1):
            for coin in coins:
                if curr_amt + coin <= amount:
                    dp[curr_amt + coin] = min(dp[curr_amt + coin], 1 + dp[curr_amt])
        
        return dp[amount] if dp[amount] != float('inf') else -1