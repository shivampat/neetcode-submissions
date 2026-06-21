from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterCounts = Counter(s)
        substrings = []

        substr = [0] * 26
        lettersSeen = set()
        currSubstrLen = 0

        for i, c in enumerate(s):
            if c not in lettersSeen:
                substr[ord(c) - ord('a')] = letterCounts[c]
                lettersSeen.add(c)
            
            substr[ord(c) - ord('a')] -= 1
            currSubstrLen += 1

            matches = 0
            for j in range(len(substr)):
                if substr[j] == 0:
                    matches += 1
            
            if matches == len(substr):
                substrings.append(currSubstrLen)
                currSubstrLen = 0

        return substrings