class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        pair = {}
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    res += 1
                    pair[i] = [nums[i], nums[j]]
        return res                


sol = Solution()
nums = [-1,1,2,3,1]
target = 2
# nums = [-6,2,5,-2,-7,-1,3]
# target = -2
ExpectedOutput = 10
Output = sol.countPairs(nums, target) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
