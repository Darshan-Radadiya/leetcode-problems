from typing import List
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(n):
            if parent[n] == n:
                return n
            else:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(x, y):
            xParent = find(x)
            yParent = find(y)
            if xParent > yParent:
                parent[yParent] = xParent
            elif xParent < yParent:
                parent[xParent] = yParent
            else:
                parent[xParent] = yParent
                rank[yParent] += 1
            
        parent = [i for i in range(27)]
        rank = [1] * 26
        for e in equations:
            if e[1] == "=":
                union((ord(e[0]) - ord('a')),(ord(e[3]) - ord('a')))

        for e in equations:
            if e[1] == "!":
                parentA = find(ord(e[0]) - ord('a'))
                parentB = find(ord(e[3]) - ord('a'))
                if parentA == parentB:
                    return False
        return True

equations = ["a==b","b!=a"]
sol = Solution()
Output = sol.equationsPossible(equations)
ExpectedOutput = False
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(N) and Space O(N)\n" )