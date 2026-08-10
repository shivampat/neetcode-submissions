class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {c:i for i, c in enumerate(s)} 
        N = len(s)
        l = 0

        windowEnd = 0
        sizes = []

        visited = set()
        for r in range(N):
            if s[r] not in visited:
                visited.add(s[r])
                windowEnd = max(windowEnd, lastSeen[s[r]])
            
            if r == windowEnd:
                sizes.append(r - l + 1)
                l = r + 1
                visited.clear() 
        
        return sizes