from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}
        n = len(graph)
        res = []
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i] = True
            return safe[i]
        
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
sol = Solution()
Output = sol.eventualSafeNodes(graph)
ExpectedOutput = [2,4,5,6]
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(N)\n" )             
