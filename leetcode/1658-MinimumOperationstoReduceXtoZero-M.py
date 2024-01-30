class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        curr_sum = 0
        res = -1
        l = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            while l <= r and curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            
            if curr_sum == target:
                res = max(res, r - l + 1)

        return -1 if res == -1 else len(nums) - res
    
sol = Solution()
nums = [1,1,4,2,3]
x = 5
# nums = [5,6,7,8,9] 
# x = 4
# ans = -1
ExpectedOutput = 2
Output = sol.minOperations(nums, x) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
