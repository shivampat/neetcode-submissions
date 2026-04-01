class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        maxArea = float('-inf')
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i == j:
                    continue
                
                maxArea = max(maxArea, min(heights[i], heights[j]) * abs(j-i))

        return maxArea
