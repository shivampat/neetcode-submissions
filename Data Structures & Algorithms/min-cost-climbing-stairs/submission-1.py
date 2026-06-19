class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        twoAway, oneAway = 0, cost[-1] 

        for i in range(n - 2, -1, -1):
            tmp = oneAway
            oneAway = min(twoAway, oneAway) + cost[i]
            twoAway = tmp
        
        return min(twoAway, oneAway)