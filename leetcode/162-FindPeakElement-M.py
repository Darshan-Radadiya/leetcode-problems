class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left =0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left + 1) //2 # Right biased mid as left = mid in else condition # prevent infinite loop
            if nums[mid] > nums[mid-1]: # True condition # go right # inc function # Last True 
                left = mid # mid is a potential elem
            else:
                right = mid -1
        return left
        
sol = Solution()
nums = [1,2,1,3,5,6,4]
ExpectedOutput = 5
Output = sol.findPeakElement(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log n) \n" )
