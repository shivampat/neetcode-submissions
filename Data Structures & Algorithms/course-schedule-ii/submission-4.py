from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqCount = [0] * numCourses
        allPrereqs = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqCount[course] += 1
            allPrereqs[prereq].append(course)
        
        q = deque([])

        for i, reqCount in enumerate(prereqCount):
            if reqCount == 0:
                q.append(i)
        
        order = []
        while q:
            for _ in range(len(q)):
                currCourse = q.popleft()
                order.append(currCourse)

                for prereq in allPrereqs[currCourse]:
                    prereqCount[prereq] -= 1
                    if prereqCount[prereq] == 0:
                        q.append(prereq)
        
        if len(order) != numCourses:
            return []
        return order