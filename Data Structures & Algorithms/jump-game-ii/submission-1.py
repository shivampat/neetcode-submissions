class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        jumps = 0

        while r < len(nums) - 1:
            maxIndx = r + 1

            while l <= r:
                maxIndx = max(maxIndx, l + nums[l])
                l += 1
            
            r = min(len(nums) - 1, maxIndx)
            jumps += 1
            
        return jumps