from collections import deque
class Node():
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

#          1 
#       /     \
#     2         3
#   /   \     /   \
# 4      5   6     7

class TraversalOFTree():
    def DFSIterative(self, root):
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            # if we swap the order of pushing child in stack it will prioritize the right side first
            # because we are pushing the left first and then right that why in stack right will be popped first.
            # right prioritize result -> [1, 3, 7, 6, 2, 5, 4]
            # for the below code its left prioritize. ->  [1, 2, 4, 5, 3, 6, 7]
            if curr.right: stack.append(curr.right)   
            if curr.left:  stack.append(curr.left)
        return res

    def DFSRecursive(self, root, res):
        if not root: return None
        res.append(root.val)
        self.DFSRecursive(root.left,res)
        self.DFSRecursive(root.right,res)
        return res

    def BFSIterative(self,root):
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr.val)
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        return res
    
    def BFSRecursive(self,root):

    # You know, maybe aside from just some superficial changes to the code style, 
    # this is going to be your go-to and only solution for a breadth-first traversal on a binary tree, right? 
    # A common mistake I see people make a lot is trying to implement a breadth-first traversal recursively.
    # And that should make sense because a breadth-first traversal needs to follow a queue order; it needs to use a queue.
    # If you write any recursive code, you know that under the hood, it's using a stack.
    # So that stack versus queue difference will really work against you, 
    # and you're going to have a tough time trying to implement the correct ordering.
    # So always just write the iterative version for your breadth-first traversal." 

        return     

    def findTheElementInBinaryTree(self, root, ele):
        if not root:
            return None
        stack = [ root ]
        
        while stack:
            node = stack.pop()
            if node.val == ele:
                return True
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return False

    def findTheElementInBinaryTreeBFS(self, root, ele):
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.val == ele:
                return True
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return False

sol = TraversalOFTree()
tree = sol.DFSIterative(root)
print("DFS - Iterative traversal of tree", tree)
tree2 = sol.DFSRecursive(root, [])
print("DFS - Recursive traversal of tree", tree2)
tree3 = sol.BFSIterative(root)
print("BFS - Iterative traversal of tree", tree3)

findEleDFS = sol.findTheElementInBinaryTree(root, 2)
print("DFS - Iterative Find element", findEleDFS)
findEleBFS = sol.findTheElementInBinaryTreeBFS(root, 2)
print("BFS - Iterative Find element", findEleBFS)


print("Time and Space complexity is O(n)")



    