class Solution:
    def findOrder(self, numCourses, prerequisites):
        
        preMap = { c:[] for c in range(numCourses)}
        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)
        print(preMap)
        
        cycle = set()
        visited = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            cycle.remove(crs)
            visited.add(crs)    
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output # for this problem we don't need to change the order.
        # return output[::-1] #printing in reverse order as we are using topological sort. 


sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
ExpectedOutput = [3,2,1,0]

numCourses = 6
prerequisites = [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]
ExpectedOutput = [5, 4, 2, 3, 1, 0]

Output = sol.findOrder(numCourses, prerequisites) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput[::-1],"\n" )
print("The output matches with expected Output: ", ExpectedOutput[::-1] == Output, "\n" )
print("Time Complexity is: O(NumOfCrs + PreReq) == O(N + P)\n" )
