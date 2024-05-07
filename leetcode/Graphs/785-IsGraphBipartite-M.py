from typing import List
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # step 2 - define BFS and check if graph is bipartite.
        def bfs(u, currColor):
            q = deque()
            q.append(u)
            color[u] = currColor
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if color[v] == color[u]:
                        return False
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
            return True

        #  Step 2 - define DFS and check if graph is bipartite.
        def dfs(u, currColor):
            color[u] = currColor
            for v in graph[u]:
                if color[v] == currColor:
                    return False
                if color[v] == -1:
                    color[v] = 1 - currColor
                    if not dfs(v, color[v]):
                        return False
            return True

        # step 1 - visit all nodes and call dfs.
        # 1 - green color
        # 0 - red color
        color = [-1] * len(graph)
        for u in range(len(graph)):
            if color[u] == -1 and not bfs(u, 1):
                return False
        return True
    
graph = [[1,2,3],[0,3,4],[0,3],[0,1,2],[1]]
sol = Solution()
Output = sol.isBipartite(graph)
ExpectedOutput = False
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(E + V) and Space O(V)\n" )