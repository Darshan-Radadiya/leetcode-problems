class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        l, r = 0, 0
        res = 0
        while l < len(nums):
            if nums[l] != 0:
                r += 1
                l += 1
            elif nums[l] == 0:
                while r < len(nums) and nums[r] == 0:
                    r += 1
                res += ( ((r - l) * ((r - l) + 1)) // 2)
                l, r = r + 1, r + 1
        return res
        
        
nums = [0,0,0,2,0,0]
sol = Solution()
Output = sol.zeroFilledSubarray(nums)
ExpectedOutput = 9
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )