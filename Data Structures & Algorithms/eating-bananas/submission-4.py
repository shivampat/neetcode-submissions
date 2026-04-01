import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = max(piles)

        while l <= r:
            m = l + ((r-l) // 2)

            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / m)
            
            if totalHours > h:
                l = m + 1
            elif totalHours <= h:
                r = m - 1
                result = m
        return result