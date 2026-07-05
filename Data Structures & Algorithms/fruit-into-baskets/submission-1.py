class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        N = len(fruits)
        start = 0
        occurences = {}

        for end in range(N):
            occurences[fruits[end]] = end

            if len(occurences) > 2:
                minF, minStart = None, float('inf')
                for f, o in occurences.items():
                    if o < minStart:
                        minF = f
                        minStart = o
                
                del occurences[minF]
                start = minStart + 1
            
            maxFruits = max(maxFruits, end - start + 1)
        
        return maxFruits