class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {char:0 for char in set(s)}
        t_count = {char:0 for char in set(t)}

        for char in s:
            s_count[char] += 1
        
        for char in t:
            t_count[char] += 1

        return s_count == t_count

            