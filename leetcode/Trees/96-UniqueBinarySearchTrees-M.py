
class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)
        # starting from 2 bcs we know for node 0 and 1 only 1 subtree possible.
        for nodes in  range(2, n + 1):
            total = 0
            for root in range(1, nodes+1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]
sol = Solution()
n = 40000
ExpectedOutput = 1767263190
Output = sol.numTrees(n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^2)\n" )

