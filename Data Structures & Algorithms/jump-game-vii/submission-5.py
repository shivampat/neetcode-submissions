class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)

        q = deque([0])
        visited = set()
        visited.add(0)

        while q:
            i = q.popleft()
            if i == N - 1:
                return True

            start, end = i + minJump, min(i + maxJump, N - 1)
            for j in range(start, end + 1):
                if s[j] == '0' and j not in visited:
                    q.append(j)
                    visited.add(j)
            
        return False