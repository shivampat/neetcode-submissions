import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones] 
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x, y = abs(heapq.heappop(heap)), abs(heapq.heappop(heap))

            if x > y:
                heapq.heappush(heap, -(x-y))
            else:
                heapq.heappush(heap, -(y-x))
        
        return abs(heap[0])