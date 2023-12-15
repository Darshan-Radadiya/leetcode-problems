class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        l = len(nums)
        for i in range(l):
            if nums[i] < 0:
                nums[i] = 0
    
        for i in range(l):
            temp = abs(nums[i])
            if 1 <= temp <= l:
                if nums[temp - 1] > 0:
                    nums[temp - 1] *= -1
                elif nums[temp - 1] == 0:
                   nums[temp - 1] = -1*(l+1)

        for i in range(1,l+1):
            if nums[i-1] >= 0:
                return i
        return l+1




sol = Solution() 
nums = [3,4,-1,1]
ExpectedOutput = 2
Output = sol.firstMissingPositive(nums)
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and space is O(1) \n" )