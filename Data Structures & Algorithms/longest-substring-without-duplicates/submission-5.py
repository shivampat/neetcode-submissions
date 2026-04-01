class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l, r = 0, 0
        c_set = set()
        maxLen = 1
        while l < len(s) and r < len(s):
            c = s[r]
            if c in c_set:
                while c in c_set:
                    c_set.remove(s[l])
                    l += 1
            c_set.add(c)
            maxLen = max(maxLen, len(c_set))
            r += 1
        
        return maxLen
            