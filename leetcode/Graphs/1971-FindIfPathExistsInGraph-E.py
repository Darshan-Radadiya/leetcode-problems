from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def createAdjacencyList(edges):
            adj = {}
            for parent, child in edges:
                if parent not in adj: adj[parent] = []
                if child not in adj: adj[child] = []
                adj[parent].append(child)
                adj[child].append(parent)
            return adj

        def hasPathUndirectedGraphDFS(graph, source, des, visited):
            if source == des:
                return True
            if source not in visited:
                visited.add(source)
                for nei in graph[source]:
                    if hasPathUndirectedGraphDFS(graph, nei, des, visited):
                        return True
            return False
        
        graph = createAdjacencyList(edges)
        visited = set()
        return hasPathUndirectedGraphDFS(graph,source, destination, visited)


sol = Solution()
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
source = 5
n = 10
destination = 9
ExpectedOutput = True
Output = sol.validPath(n, edges, source, destination) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is O(edges) and Space complexity is O(no. of nodes)")
