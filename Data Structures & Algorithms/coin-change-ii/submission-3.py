class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        allWays = {}
        def dfs(i, a):
            nonlocal amount, coins, allWays

            if (i, a) in allWays:
                return allWays[(i, a)]

            if a > amount:
                return 0
            
            if a == amount:
                return 1

            ways = 0
            for i in range(i, len(coins)):
                allWays[(i, a + coins[i])] = dfs(i, a + coins[i]) 
                ways += allWays[(i, a + coins[i])]

            return ways
        
        return dfs(0, 0)