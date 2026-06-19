class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def robSubarray(start, end):
            two = one = 0

            for i in range(start, end + 1):
                two, one = one, max(two + nums[i], one)
            
            return one

        return max(robSubarray(0, len(nums) - 2), robSubarray(1, len(nums) - 1))