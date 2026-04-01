class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            m = numbers[r] + numbers[l] 

            if m > target:
                r -= 1
            elif m < target: 
                l += 1
            else:
                break

        return [l+1, r+1]