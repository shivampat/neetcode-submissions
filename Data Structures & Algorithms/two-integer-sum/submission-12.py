class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for i, n in enumerate(nums):
            if n in diffMap:
                return [diffMap[n], i]
            diffMap[target - n] = i
            print(diffMap)
        
        return [0, 0]