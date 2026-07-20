class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {}

        def dfs(curr_sum):
            nonlocal target, nums, dp
            if curr_sum in dp:
                return dp[curr_sum]

            if curr_sum == target:
                return 1

            total = 0 
            for num in nums:
                if curr_sum + num > target:
                    break

                total += dfs(curr_sum + num)
                
            dp[curr_sum] = total
            
            return total
        
        return dfs(0)
            
