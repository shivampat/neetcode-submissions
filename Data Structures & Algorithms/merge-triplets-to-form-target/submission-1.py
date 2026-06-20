class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        skip = set()
        for i, trip in enumerate(triplets):
            for x, y in zip(trip, target):
                if x > y:
                    skip.add(i)
                    break

        hasNum = [False, False, False] 
        for i, trip in enumerate(triplets):
            if i in skip:
                continue
            
            for i, a in enumerate(zip(trip, target)):
                x, y = a
                if x == y:
                    hasNum[i] = True
        
        return hasNum == [True] * 3
