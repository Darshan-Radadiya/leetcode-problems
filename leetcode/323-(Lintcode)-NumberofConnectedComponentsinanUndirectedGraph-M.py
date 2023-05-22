# For this problem we used Union find by RANK which is 
# a data structure and algorithm used to track and 
# efficiently manipulate disjoint sets of elements.
# Union-Find is primarily used for disjoint set operations and connectivity problems, 
# while DFS and BFS are graph traversal algorithms used for exploring and searching in graphs. 
# union find - https://www.youtube.com/watch?v=aBxjDBC4M1U&ab_channel=takeUforward

class Solution:
  def countComponents(self, n: int, edges):
    par = [i for i in range(n)]
    rank = [1]*n

    def find(n1):
      parent = n1
      while parent != par[parent]:
        par[parent] = par[par[parent]] # path compression
        parent = par[parent]
      return parent
    
    def union(n1, n2):
      parOfn1, parOfn2 = find(n1), find(n2)

      if parOfn1 == parOfn2:
        return 0
      if rank[parOfn1] > rank[parOfn2]:
        par[parOfn2] = parOfn1
        rank[parOfn2] += rank[parOfn1]
      else:
        par[parOfn1] = parOfn2
        rank[parOfn1] += rank[parOfn2]
    
      return 1

    numOfDisJoint = n
    for e1, e2 in edges:
      numOfDisJoint -= union(e1, e2)
    return numOfDisJoint

sol = Solution()
# n = 5
# edges = [[0,1],[1,2],[3,4]]

n = 6
edges = [[0, 1], [1, 2], [3, 4], [4, 5]]

ExpectedOutput = 2
Output = sol.countComponents(n, edges) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(Edges + Vertices) == O(|E| + |V|)\n" )
