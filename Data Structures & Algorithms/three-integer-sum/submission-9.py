class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        ans = []
        for i in range(len(nums)-1):
            target = nums[i]

            # skip already used targets
            if i > 0 and target == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                num_sum = target + nums[l] + nums[r]
                if num_sum < 0:
                    l += 1
                elif num_sum > 0:
                    r -= 1
                else:
                    ans.append([target, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < len(nums)-1 and nums[l-1] == nums[l]:
                        l += 1

        return ans