class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        # DP similar to 152 maximumProductSubarray
        # res = max(nums)
        # curMax, curMin = 0, 0 
        # for n in nums:
        #     temp = curMax + n
        #     curMax = max(temp, curMin+n, n)
        #     curMin = min(temp, curMin+n, n)
        #     res = max(curMax, res)
        # return res

        # Greedy
        res = max(nums)
        curSum = 0 
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            res = max(curSum, res)
        return res
    


sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
ExpectedOutput = 6
Output = sol.maxSubArray(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
