class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digMap = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }

        combinations = []
        
        currComb = []
        def dfs(i):
            if i >= len(digits):
                combinations.append(''.join(currComb))
                return
            
            for letter in digMap[digits[i]]:
                currComb.append(letter)
                dfs(i + 1)
                currComb.pop()
        
        dfs(0)
        return combinations