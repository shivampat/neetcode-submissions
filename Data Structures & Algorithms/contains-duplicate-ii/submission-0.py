from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupIndx = defaultdict(int)

        for i, num in enumerate(nums):
            if num in dupIndx:
                if abs(i - dupIndx[num]) <= k:
                    return True
                
            dupIndx[num] = i
        
        return False
            