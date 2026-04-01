class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)

        prefix_prod = 1
        for i in range(len(nums)):
            output[i] *= prefix_prod
            prefix_prod *= nums[i]
        suffix_prod = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= suffix_prod
            suffix_prod *= nums[j]
        return output
