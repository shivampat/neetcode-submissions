class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        all_subsets = []

        def subsets(i, s):
            if i >= len(nums):
                all_subsets.append(s.copy())
                return
            
            s.append(nums[i])
            subsets(i + 1, s)

            s.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            subsets(i + 1, s)
        
        subsets(0, [])
        
        return all_subsets