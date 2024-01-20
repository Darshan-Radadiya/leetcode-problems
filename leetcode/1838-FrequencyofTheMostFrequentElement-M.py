class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, 0
        res, total = 0, 0

        while r < len(nums):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res
        
nums = [1,4,8,13]
k = 5
ExpectedOutput = 2
Output = sol.maxFrequency(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(nlogn)\n" )

