# ref: https://leetcode.com/problems/combination-sum/solutions/1777569/full-explanation-with-state-space-tree-recursion-and-backtracking-well-explained-c/

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        currentCandidates = []
        def dfs(i, total):

            if total == target:
                res.append(currentCandidates.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            currentCandidates.append(candidates[i])
            dfs(i, total + candidates[i])
            currentCandidates.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return res

candidates = [2,3,6,7]
target = 7
sol = Solution()
Output = sol.combinationSum(candidates,target)
ExpectedOutput = [[2, 2, 3], [7]]
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(2^target)\n" )

