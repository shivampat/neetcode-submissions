class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0]) 

        merged = []

        currInt = intervals[0]

        for i in range(len(intervals)):
            startI, endI = intervals[i]
            startCurr, endCurr = currInt

            if endCurr < startI:
                merged.append(currInt)
                currInt = intervals[i]
                continue
            
            currInt = [startCurr, max(endI, endCurr)]
        
        merged.append(currInt)

        return merged