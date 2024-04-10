# ref:- https://www.youtube.com/watch?v=Vd2YizhbN74&ab_channel=codestorywithMIK
from typing import List
class Solution:
    def permute(self, idx, nums, res):
        if idx == len(nums):
            res.append(nums.copy())
            return
        sameEle = set()
        for i in range(idx, len(nums)): 
            if nums[i] not in sameEle:        
                sameEle.add(nums[i])
                nums[i], nums[idx] = nums[idx], nums[i]
                self.permute(idx+1, nums, res)
                nums[i], nums[idx] = nums[idx], nums[i]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.permute(0, nums, res)
        return res
    

nums = [1,1,2]
sol = Solution()
Output = sol.permuteUnique(nums)
ExpectedOutput = [[1,1,2],[1,2,1],[2,1,1]]
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n * n!) n for adding ele in res and n! for the FOR loop\n" )

