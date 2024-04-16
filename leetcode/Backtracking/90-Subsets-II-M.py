from typing import List
class Solution:
    def dfs(self, i, subsets, res, nums):
        if i >= len(nums):
            res.append(subsets.copy())
            return 
        
        # we will consider nums[i]
        subsets.append(nums[i])
        self.dfs(i + 1, subsets, res, nums)

        # we will not consider the nums[i]
        subsets.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.dfs(i + 1, subsets, res, nums)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        self.dfs(0, subset, res, nums)
        return res

sol = Solution()
nums = [1,2,3,3, 5]
ExpectedOutput = [[1, 2, 3, 3, 5], [1, 2, 3, 3], [1, 2, 3, 5], [1, 2, 3], [1, 2, 5], [1, 2], [1, 3, 3, 5], [1, 3, 3], [1, 3, 5], [1, 3], [1, 5], [1], [2, 3, 3, 5], [2, 3, 3], [2, 3, 5], [2, 3], [2, 5], [2], [3, 3, 5], [3, 3], [3, 5], [3], [5], []] 
Output = sol.subsetsWithDup(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O( (n log n) + (n * 2^n))\n" )