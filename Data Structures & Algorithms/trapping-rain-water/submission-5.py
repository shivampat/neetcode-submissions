class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force 
        total_area = 0
        for i in range(len(height)):
            maxl = 0
            maxr = 0
            for l in range(i):
                maxl = max(maxl, height[l])
            for r in range(i+1, len(height)):
                maxr = max(maxr, height[r])

            total_area += max(min(maxl, maxr) - height[i], 0)
        
        return total_area