class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpCount = 0
        for i in range(len(nums) - 1, -1, -1):
            if jumpCount <= nums[i]:
                jumpCount = 0
            jumpCount += 1

        return jumpCount == 1 