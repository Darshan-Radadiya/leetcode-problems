from typing import List
from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # T and S is O(n)
        def createADJList(edges):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        adjList = createADJList(edges)
        for key in adjList:
            if len(adjList[key]) == len(adjList) - 1:
                return key

        # we have given n-1 edges for n nodes that's why 
        # we can use below code to find the common node between first two edges.
        # T and S is O(1)
        first_edge, second_edge = edges[0], edges[1]

        return first_edge[0] if first_edge[0] in second_edge else first_edge[1]

sol = Solution()
edges = [[1,2],[5,1],[1,3],[1,4]]
ExpectedOutput = 1
Output = sol.findCenter(edges) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
