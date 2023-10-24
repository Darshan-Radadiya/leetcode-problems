class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Moore's Voting Algorithm
        res = nums[0]
        count = 0
        for i in range(len(nums)):
            if count == 0:
                res = nums[i]
            if res == nums[i]:
                count += 1
            else:
                count -= 1
        return res
            

sol = Solution()
nums = [2,2,1,1,1,2,2]
ExpectedOutput = 2
Output = sol.majorityElement(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space O(1)\n" )


        