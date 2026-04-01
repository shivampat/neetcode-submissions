class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            lookFor = target - numbers[i]
            for j in range(i + 1, len(numbers)):
                if lookFor == numbers[j]:
                    return list((i+1, j+1))