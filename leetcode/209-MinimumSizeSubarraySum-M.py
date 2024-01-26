class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        r, l, res = 0, 0, float("inf")
        total = 0
        while r < len(nums):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
            else:
                r += 1
        return res if res != float("inf") else 0

nums = [2,3,1,2,4,3]
k = 7
sol = Solution()
Output = sol.minSubArrayLen(k, nums) 
ExpectedOutput = 2
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(nlogn)\n" )

