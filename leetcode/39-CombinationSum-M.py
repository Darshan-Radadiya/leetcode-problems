# ref: https://leetcode.com/problems/combination-sum/solutions/1777569/full-explanation-with-state-space-tree-recursion-and-backtracking-well-explained-c/

class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, currentCandidates, total):

            if total > target or i >= len(candidates):
                return
            if total == target:
                res.append(currentCandidates.copy())
                return
            
            currentCandidates.append(candidates[i])
            dfs(i, currentCandidates, total + candidates[i])
            currentCandidates.pop()
            dfs(i+1, currentCandidates, total)

        dfs(0, [], 0)
        return res

candidates = [2,3,6,7]
target = 7
Output = [[2, 2, 3], [7]]
sol = Solution()
print("Expected Output:", Output)
print("Output: ",sol.combinationSum(candidates,target))

