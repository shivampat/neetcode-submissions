class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLength = 0

        l, r = 0, 0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
            r += 1
        
        return maxLength
                
            
