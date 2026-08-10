class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        N = len(nums)

        def dfs(i, curr_sum):
            nonlocal N, target

            if curr_sum == target:
                return True
            if i >= N or curr_sum > target:
                return False

            # Case: include number or Case skip number
            return dfs(i + 1, curr_sum + nums[i]) or \
            dfs(i + 1, curr_sum)
        
        return dfs(0, 0)

            