# Python program for
# validation of a graph

# import dictionary for graph
from collections import defaultdict

# function for adding edge to graph
graph = defaultdict(list)
def addEdge(graph,u,v):
	graph[u].append(v)

# definition of function
def generate_edges(graph):
	edges = []

	# for each node in graph
	for node in graph:
		
		# for each neighbour node of a single node
		for neighbour in graph[node]:
			
			# if edge exists then append
			edges.append([node, neighbour])
	return edges

# declaration of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

# Driver Function call
# to print generated graph
print(generate_edges(graph))




# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy 
        
        return clone(node) if node else None

node = [[2,4],[1,3],[2,4],[1,3]]
Output = [[2,4],[1,3],[2,4],[1,3]]
sol = Solution()
print("Expected Output:", Output)
print("Output: ",sol.cloneGraph(node))  