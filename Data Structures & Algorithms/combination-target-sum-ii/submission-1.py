class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        results = []

        def dfs(i, subset, currSum):
            if i >= len(candidates) or currSum >= target:
                if currSum == target:
                    results.append(subset.copy())
                return
            
            # Include current element
            subset.append(candidates[i])
            dfs(i + 1, subset, currSum + candidates[i])


            # Skip current element and neighbors is neighbors are same
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, subset, currSum)
        
        dfs(0, [], 0)

        return results

     