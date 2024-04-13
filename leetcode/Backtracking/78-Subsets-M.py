from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                # In Python, when you assign a list to another variable or pass it as an argument to a function,
                # it creates a reference to the same list object in memory. So, if you were to directly append 
                # chosen to res without creating a copy, any modifications made to chosen later on would also 
                # reflect in the already appended lists in res.
                res.append(subset.copy())
                return 
            
            # we will consider nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # we will not consider the nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

sol = Solution()
nums = [1,2,3,5]
ExpectedOutput = [[1, 2, 3, 5], [1, 2, 3], [1, 2, 5], [1, 2], [1, 3, 5], [1, 3], [1, 5], [1], [2, 3, 5], [2, 3], [2, 5], [2], [3, 5], [3], [5], []]
Output = sol.subsets(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n * 2^n)\n" )
