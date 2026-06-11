import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return math.sqrt(point[0]**2 + point[1]**2)
        
        closest = []
        heapq.heapify(closest)

        for pt in points:
            heapq.heappush(closest, (-distance(pt), pt))
            if len(closest) > k:
                heapq.heappop(closest)

        return [i[1] for i in closest]

