from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
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
        
        if len(connections) < (n-1):
            return -1
        parent = [i for i in range(n)]
        rank = [1] * n
        component = n
        for a, b in connections:
            aParent = find(a)
            bParent = find(b)
            if aParent == bParent:
                continue
            else:
                component -= 1
                union(aParent, bParent)
        print(rank)
        return component - 1
    
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
sol = Solution()
Output = sol.makeConnected(n, connections)
ExpectedOutput = 2
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(N) and Space O(N)\n" )