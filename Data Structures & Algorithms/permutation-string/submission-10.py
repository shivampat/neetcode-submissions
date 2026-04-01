class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = {}
        window = {}

        for c in s1:
            counts[c] = counts.get(c, 0) + 1
        
        for c in s2:
            counts[c] = counts.get(c, 0)
            window[c] = 0
        
        for i in range(len(s1)):
            window[s2[i]] += 1

        l, r = 0, len(s1)-1
        while r < len(s2):
            correct = 0
            for char in window:
                if window[char] == counts[char]:
                    correct += 1
            
            if correct == len(counts.keys()):
                return True
            
            window[s2[l]] -= 1
            print(s2[l:r+1])
            print(window)
            print(counts)
            l += 1
            r += 1
            if r < len(s2):
                window[s2[r]] += 1
        
        return False