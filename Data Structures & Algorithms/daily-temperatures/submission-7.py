class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N
        stack = [] # (i, temp)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, prevTmp = stack.pop()
                res[j] = i - j
            
            stack.append((i, temp))
        
        return res