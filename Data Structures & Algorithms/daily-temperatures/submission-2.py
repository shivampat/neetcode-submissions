class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        ans = []
        for i in range(len(temperatures)):
            indx = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    indx = j-i
                    break
            ans.append(indx) 
        return ans