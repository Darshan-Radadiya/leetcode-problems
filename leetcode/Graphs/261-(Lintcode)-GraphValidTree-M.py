class Solution():
    # Union Find Algorithm
    def graphValidTree(self, n, edges):
        parent = [i for i in range(n)]
        ranks = [i for i in range(n)]

        # Build Find
        def find(n1):
            p = parent[n1]
            while p != parent[p]:
                parent[p] = parent[parent[p]] # Path Compression 
                p = parent[p]
            return p

        # Build Union
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if ranks[p1] > ranks[p2]:
                ranks[p1] += ranks[p2]
                parent[p2] = p1
            else:
                ranks[p2] += ranks[p1]
                parent[p1] = p2
            return True

        for n1, n2 in edges:
            if union(n1, n2):
                n -= 1
            else:
                return False
        return n == 1

    # Using DFS. 
    def graphValidTree(self,n, edges):

        edgeMap = {i:[] for i in range(n)}

        # Appending both n1 and n2 because we have given undirected graph.
        for n1, n2 in edges:
            edgeMap[n1].append(n2)
            edgeMap[n2].append(n1)
        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for adj in edgeMap[node]:
                if adj == prev: continue
                if not dfs(adj, node):
                    return False
            return True
        return dfs(0, -1) and n == len(visited)

sol = Solution()

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

ExpectedOutput = True
Output = sol.graphValidTree(n,edges)
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(Edges + Vertices) == O(|E| + |V|)\n" )