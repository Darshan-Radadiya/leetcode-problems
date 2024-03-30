from typing import List
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i : [] for i in range(n)}
        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        print(adj)

        def dfs(curr, parent):
            time = 0
            for child in adj[curr]:
                if child == parent:
                    continue
                childTime = dfs(child, curr)
                if childTime or hasApple[child]:
                    time += childTime + 2
            return time
        return dfs(0, -1)

sol = Solution()
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
ExpectedOutput = 8
Output = sol.minTime(n, edges, hasApple) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
