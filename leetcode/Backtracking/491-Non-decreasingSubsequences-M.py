from typing import List
class Solution:
    def backtrack(self, nums, idx, currSubSeq, res):
        if len(currSubSeq) >= 2:
            res.append(currSubSeq.copy())
            
        used = set()
        for i in range(idx, len(nums)):
            if (not currSubSeq or (currSubSeq and nums[i] >= currSubSeq[-1])) and nums[i] not in used:
                currSubSeq.append(nums[i])
                self.backtrack(nums, i+1, currSubSeq, res)
                currSubSeq.pop()
                used.add(nums[i])
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, 0, [], res)
        return res

nums = [4,6,7,7]
sol = Solution()
Output = sol.findSubsequences(nums)
ExpectedOutput = [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n * 2^n) n for adding ele in res\n" )
