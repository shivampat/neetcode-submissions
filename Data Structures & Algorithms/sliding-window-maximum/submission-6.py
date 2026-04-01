class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums)-k+1):
            winMax = nums[i]
            for j in range(i, i + k):
                winMax = max(winMax, nums[j])
            print(nums[i:i+k])
            ans.append(winMax)
        return ans
            