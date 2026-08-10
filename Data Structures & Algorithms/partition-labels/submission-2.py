class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {c:i for i, c in enumerate(s)} 
        N = len(s)
        l = 0

        windowEnd = 0
        sizes = []

        for r in range(N):
            windowEnd = max(windowEnd, lastSeen[s[r]])
            
            if r == windowEnd:
                sizes.append(r - l + 1)
                l = r + 1
        
        return sizes