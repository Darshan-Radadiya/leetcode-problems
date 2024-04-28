import heapq
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #  minimum cost to make all points connected. - hint - it means its MST problem
        # MST - Minimum Spanning Tree
        adj = [[] for i in range(len(points))]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                manDist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                adj[i].append((j,manDist))
                adj[j].append((i,manDist))

        cost = 0
        visited = [False]*len(points)
        pq = []
        heapq.heappush(pq, (0, 0))
        while pq:
            dist, node = heapq.heappop(pq)
            if visited[node]:
                continue
            visited[node] = True
            cost += dist

            for v, w in adj[node]:
                if not visited[v]:
                    heapq.heappush(pq, (w, v)) 
        return cost

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
sol = Solution()
Output = sol.minCostConnectPoints(points)
ExpectedOutput = 20
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(N^2) and Space O(N)\n" )