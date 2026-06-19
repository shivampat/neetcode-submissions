class Solution:
    def rob(self, nums: List[int]) -> int:
        # [5, 1, 2, 10] 
        n = len(nums) 
        if n <= 1:
            return nums[0]
        
        two, one = nums[0], max(nums[1], nums[0])

        for i in range(2, n):
            two, one = one, max(two + nums[i], one)
        
        return one
        

