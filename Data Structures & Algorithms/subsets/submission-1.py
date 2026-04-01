class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return 
            
            # To include
            subset.append(nums[i])
            dfs(i + 1)


            # To not include
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        
        return result