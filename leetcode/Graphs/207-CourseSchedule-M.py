from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # Cycle detection in DG.
        def dfs(u):
            visited.add(u)
            inRecursion.add(u)
            for v in adj[u]:
                if v not in visited and dfs(v):
                    return True
                elif v in inRecursion:
                    return True
            inRecursion.remove(u)
            return False
        
        adj = defaultdict(list)
        for i in range(numCourses):
            adj[i] = []
        for crs, preReq in prerequisites:
            adj[preReq].append(crs)
        
        visited = set()
        inRecursion = set()
        for i in range(numCourses):
            if i not in visited and dfs(i):
                return False
        return True
        
        # preMap = { i:[] for i in range(numCourses)}
        preMap = defaultdict(list)
        for i in range(numCourses):
            preMap[i] = []
        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


sol = Solution()
numCourses = 5
prerequisites = [[1,0], [2,0], [3,1], [4,3], [4,1]]
ExpectedOutput = True
Output = sol.canFinish(numCourses, prerequisites) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(NumOfCrs + PreReq) == O(N + P)\n" )
