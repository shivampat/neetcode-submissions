class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, winCnt = {}, {}
        minLen = float('inf')
        indx = [-1, -1]

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
            winCnt[c] = 0
        
        matches = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in winCnt:
                continue
            
            if winCnt[s[i]] + 1 == t_count[s[i]]:
                matches += 1
            winCnt[s[i]] += 1

            while matches == len(t_count.keys()):
                if i - l + 1 < minLen:
                    indx[0], indx[1] = l, i
                    minLen = i - l + 1
                if s[l] in winCnt:
                    winCnt[s[l]] -= 1
                    if winCnt[s[l]] < t_count[s[l]]:
                        matches -= 1
                l += 1
            
        if minLen == float('inf'):
            return ""
        
        return s[indx[0]:indx[1]+1]




            

                