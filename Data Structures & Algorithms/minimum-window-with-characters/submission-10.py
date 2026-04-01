class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        minStr = None

        t_counts = {}
        for c in t:
            t_counts[c] = 1 + t_counts.get(c, 0)

        w_counts = {c:0 for c in t_counts}
        l, r = 0, 0
        while r < len(s):
            if s[r] in t_counts:
                w_counts[s[r]] += 1

            
            while True:
                while l < r and s[l] not in t_counts:
                    l += 1
                
                numCorrect = 0
                for c in w_counts:
                    if w_counts[c] >= t_counts[c]:
                        numCorrect += 1
                
                if numCorrect == len(t_counts.keys()):
                    if minStr is None or len(minStr) > (r-l+1):
                        minStr = s[l:r+1]
                    if s[l] in t_counts:
                        w_counts[s[l]] -= 1
                    l += 1
                else:
                    break
            
            r += 1

        if minStr is not None:
            return minStr
        else:
            return ""
