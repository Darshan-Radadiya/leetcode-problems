class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        subSequences = 0
        mod = (10 ** 9 + 7)
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] + nums[r] <= target:
                subSequences += 2 ** (r - l)
                subSequences %= mod
                l += 1
            else:
                r -= 1
        return subSequences

nums = [7,10,7,3,7,5,4]
target = 12
ExpectedOutput = 56
sol = Solution()
Output = sol.numSubseq(nums, target) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )
