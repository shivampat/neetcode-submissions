class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while stack:
                top_tmp, top_indx = stack[-1]
                if temperatures[i] > top_tmp:
                    ans[top_indx] = i-top_indx
                    stack.pop()
                else:
                    break
            stack.append((temperatures[i], i))
        return ans
            
        