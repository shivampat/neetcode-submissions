from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        start = 0

        for end in range(len(nums)):
            while start < end and end - start > k:
                window.remove(nums[start])
                start += 1
            
            if nums[end] in window:
                return True
            
            window.add(nums[end])
        
        return False
