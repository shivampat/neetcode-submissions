class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_i = len(nums) - k
        l, r = 0, len(nums) - 1

        while True:
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p] 

            if p < k_i:
                l = p + 1
            elif p > k_i:
                r = p - 1
            else:
                return nums[p]
            