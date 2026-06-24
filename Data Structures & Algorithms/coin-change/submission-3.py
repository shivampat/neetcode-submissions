from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        q = deque([amount])
        dp = [float('inf')] * (amount + 1)
        visited = set()

        coinsUsed = 0
        while q:
            for i in range(len(q)):
                currAmt = q.popleft()

                for coin in coins:
                    if currAmt - coin >= 0 and currAmt - coin not in visited:
                        dp[currAmt - coin] = 1 + coinsUsed
                        q.append(currAmt - coin)
                        visited.add(currAmt - coin)
            coinsUsed += 1
        
        return dp[0] if dp[0] != float('inf') else -1
        