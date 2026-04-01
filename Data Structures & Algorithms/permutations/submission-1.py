class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def calcPerm(nums):
            if len(nums) <= 0:
                return [[]]
            
            left = nums[0]
            right = nums[1:]

            perms = calcPerm(right)
            newPerms = []

            for perm in perms:
                for i in range(len(perm) + 1):
                    p_copy = perm.copy()
                    p_copy.insert(i, left)
                    newPerms.append(p_copy)
            
            return newPerms
        
        return calcPerm(nums)