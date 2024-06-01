from typing import List
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        
        def solve(idx, isEven):
            if idx >= n:
                return 0
            if (idx, isEven) in dp:
                return dp[(idx, isEven)]

            skip = solve(idx+1, isEven)
            val = nums[idx] if isEven else -1 * nums[idx]
            keep = solve(idx+1, not isEven) + val
            dp[(idx, isEven)] = max(skip, keep)
            return dp[(idx, isEven)]
        return solve(0, True)

sol = Solution()
nums = [6,2,1,2,4,5]
ExpectedOutput = 10
Output = sol.maxAlternatingSum(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(2*n)\n" )
