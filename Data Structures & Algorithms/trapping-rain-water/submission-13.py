class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) time, O(n) space
        if len(height) < 3:
            return 0

        maxl, maxr = [0] * len(height), [0] * len(height) 
        curr_maxl, curr_maxr = 0, 0

        for i in range(len(height)):
            maxl[i] = curr_maxl
            maxr[len(height)-1-i] = curr_maxr
            curr_maxl = max(curr_maxl, height[i])
            curr_maxr = max(curr_maxr, height[len(height)-1-i])
        
        print(maxl)
        print(maxr)
        
        total_area = 0
        for i in range(len(height)):
            total_area += max(min(maxl[i], maxr[i]) - height[i], 0)
        return total_area
