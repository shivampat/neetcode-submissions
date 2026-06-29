class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force:
        # take all subarrays, compute area, find max area among all subarrays
        N = len(heights)
        maxArea = 0

        for start in range(N):
            minHeight = heights[start]
            for end in range(start, N):
                minHeight = min(minHeight, heights[end])
                currArea = minHeight * (end - start + 1)
                maxArea = max(maxArea, currArea)
        
        return maxArea