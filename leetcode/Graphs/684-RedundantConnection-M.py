from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(n):
            if parent[n] == n:
                return n
            else:
                parent[n] = find(parent[n])
            return parent[n]

        def union(x, y):
            xParent = find(x)
            yParent = find(y)

            if xParent == yParent:
                return
            if rank[xParent] > rank[yParent]:
                parent[yParent] = xParent
            elif rank[xParent] < rank[yParent]:
                parent[xParent] = yParent
            else:
                parent[yParent] = xParent
                rank[xParent] += 1

        res = edges[0]
        for e1, e2 in edges:
            e1Parent, e2Parent = find(e1), find(e2)
            if e1Parent == e2Parent:
                res = [e1,e2]
            else:
                union(e1, e2)
        return res
    
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
ExpectedOutput = [1,4]
sol = Solution()
Output = sol.findRedundantConnection(edges) 
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(Edges + Vertices) == O(|E| + |V|)\n" )
