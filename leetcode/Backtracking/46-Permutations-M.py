# ref:- https://www.youtube.com/watch?v=T8hqjK94Fig&ab_channel=codestorywithMIKx
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx):
            if idx == len(nums):
                res.append(nums.copy())
                return
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]
        dfs(0)
        return res
    
        # using extra space.
        # space complexity is  O(n)
        res = []
        perm = []
        used = [False] * len(nums)  # Track if element at index i is used in the current permutation

        def recursivePermutation():
            if len(perm) == len(nums):
                res.append(perm.copy())  # Append a copy of perm to res
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    perm.append(nums[i])
                    recursivePermutation()
                    perm.pop()
                    used[i] = False

        recursivePermutation()
        return res

nums = [1,2,3]
sol = Solution()
Output = sol.permute(nums)
ExpectedOutput = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n * n!) n for adding ele in res and n! for the FOR loop\n" )

