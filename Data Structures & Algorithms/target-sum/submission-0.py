class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, a):
            if i >= len(nums):
                if a == target:
                    return 1
                return 0
            
            return dfs(i + 1, a + nums[i]) + dfs(i + 1, a - nums[i])
        
        return dfs(0, 0)