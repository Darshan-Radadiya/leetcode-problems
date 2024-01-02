class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        res = float("inf")
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        return res


sol = Solution()
nums = [9,4,1,7]
k = 2
ExpectedOutput = 2
Output = sol.minimumDifference(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n)\n" )
