class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = nums
        for i in range(len(nums)):
            print(nums[i], "i am arr", res)
            res.append(nums[i])
        return res



sol = Solution()
nums = [1,2,1]
ExpectedOutput = [1,2,1,1,2,1]
Output = sol.getConcatenation(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
