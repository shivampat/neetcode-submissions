class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            counts = [0] * 26

            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            counts = tuple(counts)
            if counts not in groups:
                groups[counts] = []
            groups[counts].append(s)
        
        return list(groups.values())