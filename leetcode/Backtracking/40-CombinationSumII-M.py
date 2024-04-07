from typing import List
class Solution:
    def backTracking(self, i , candidates, res, currentCandidates, total):
        if total == target:
            res.append(currentCandidates.copy())
            return
        if total > target or i >= len(candidates):
            return
        
        currentCandidates.append(candidates[i])
        self.backTracking(i+1, candidates, res, currentCandidates, total + candidates[i])
        currentCandidates.pop()
        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        self.backTracking(i+1, candidates, res, currentCandidates, total )
        
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backTracking(0, candidates, res, [], 0)
        return res
    
candidates = [10,1,2,7,6,1,5]
target = 8
sol = Solution()
Output = sol.combinationSum2(candidates,target)
ExpectedOutput = [
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(2^target)\n" )

