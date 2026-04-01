class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        opposites = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in opposites:
                return [opposites[num], i]
            else:
                opposites[target-num] = i
