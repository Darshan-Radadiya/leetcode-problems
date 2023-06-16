class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # brute force O(n^2)
        DP = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    DP[i] = max(DP[i], DP[j] + 1)
        return max(DP)




sol = Solution()
nums = [10,9,2,5,3,7,101,18]
ExpectedOutput = 4
Output = sol.lengthOfLIS(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^2)\n" )
