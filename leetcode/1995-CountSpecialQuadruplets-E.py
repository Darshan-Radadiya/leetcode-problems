class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    for l in range(k, n):
                        if nums[i] <= nums[j] <= nums[k] and nums[i] + nums[j] + nums[k] == nums[l]:
                            res += 1
        return res//(n-1)



sol = Solution()
# nums = [3,3,6,4,5]
# nums = [1,1,1,3,5]
# nums = [1,2,3,6]
nums = [2,16,9,27,3,39]
ExpectedOutput = 4
Output = sol.countQuadruplets(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^4)\n" )
