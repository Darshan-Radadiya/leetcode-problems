from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Optimal Space O(1)
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1

            if nums[idx] > 0:
                nums[idx] *= -1
        res = []

        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res

        # Space and time is O(n)
        disappearedSet = set()
        for i in range(1,len(nums)+1):
            disappearedSet.add(i)

        for i in range(len(nums)):
            if nums[i] in disappearedSet:
                disappearedSet.remove(nums[i])
        return disappearedSet

sol = Solution()
nums = [4,3,2,7,8,2,3,1]
ExpectedOutput = [5, 6]
Output = sol.findDisappearedNumbers(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
