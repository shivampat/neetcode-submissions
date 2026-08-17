class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # recurisve solution
        dp = {}

        def dfs(i, total):
            nonlocal amount, coins
            if (i, total) in dp:
                return dp[(i,total)]
            if total > amount:
                return 0
            if total == amount:
                return 1
            
            occurs = 0
            for j in range(i, len(coins)):
                occurs += dfs(j, total + coins[j])
            dp[(i, total)] = occurs 
            return occurs
        
        return dfs(0, 0)


