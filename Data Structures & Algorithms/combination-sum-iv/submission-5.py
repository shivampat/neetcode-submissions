class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        dp = [0] * (target + 1)

        if target == 0:
            return 1

        for num in nums:
            if num <= target:
                dp[num] = 1

        for curr_tgt in range(target + 1):
            for num in nums:
                if curr_tgt + num <= target:
                    dp[curr_tgt + num] += dp[curr_tgt] 
                else:
                    break
                
        return dp[target]

