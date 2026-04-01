class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() 

        result = []
        currSet = []

        def dfs(i):
            if i >= len(nums):
                return 
            if sum(currSet) >= target:
                if sum(currSet) == target:
                    result.append(currSet.copy())
                return
            
            # Duplicate curr number
            currSet.append(nums[i])
            dfs(i)

            # Move onto next number
            currSet.pop()
            dfs(i + 1)
        
        dfs(0)

        return result