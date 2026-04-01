class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        max_area = 0
        l, r = 0, len(heights)-1
        while l < r:
            new_area = (r-l) * min(heights[l], heights[r])
            max_area = max(max_area, new_area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_area
            