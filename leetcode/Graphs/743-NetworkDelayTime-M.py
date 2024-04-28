from typing import List
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            adj[u].append((v, w))
        pq = []
        res = [float("inf")] * (n + 1)
        res[k] = 0
        heapq.heappush(pq, (0, k))
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > res[node]:
                continue
            for adjNode, w in adj[node]:
                newDist = dist + w
                if newDist < res[adjNode]:
                    res[adjNode] = newDist
                    heapq.heappush(pq, (newDist, adjNode))
        minTime = -1
        for i in range(1, len(res)):
            if res[i] == float("inf"):
                return -1
            minTime = max(res[i], minTime)
        return minTime

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
sol = Solution()
Output = sol.networkDelayTime(times, n, k)
ExpectedOutput = 2
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(N) and Space O(N)\n" )

# Related questions:
# 787. Cheapest Flights Within K Stops
# 778. Swim in Rising Water
# 815. Bus Routes
# 1091. Shortest Path in Binary Matrix
# 1631. Path With Minimum Effort
# 2812. Find the Safest Path in a Grid
# 2642. Design Graph With Shortest Path Calculator