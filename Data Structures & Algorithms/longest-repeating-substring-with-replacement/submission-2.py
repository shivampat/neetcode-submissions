class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l, r = 0, 0
        maxLen = 0
        while l < len(s) and r < len(s):
            counts[s[r]] += 1
            
            maxCount = 1
            for c in counts:
                maxCount = max(maxCount, counts[c])
            
            while r - l + 1 - maxCount > k:
                counts[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
            r += 1
        
        return maxLen



                
