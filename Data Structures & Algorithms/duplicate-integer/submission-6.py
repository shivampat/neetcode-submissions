class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = set()

        for num in nums:
            if num in appeared:
                return True 
            else:
                appeared.add(num)
        
        return False