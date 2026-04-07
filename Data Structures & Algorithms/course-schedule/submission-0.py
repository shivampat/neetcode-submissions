class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        allPrereqs = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            allPrereqs[a].append(b)

        visited = set()
        def dfs(course):
            if not allPrereqs[course]:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)
            for req in allPrereqs[course]:
                if not dfs(req):
                    return False
            visited.remove(course)
            return True
            
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            allPrereqs[course] = []
        
        return True