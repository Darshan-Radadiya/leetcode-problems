# Description
# Given an unsorted array nums, reorder it in-place such that

# nums[0] <= nums[1] >= nums[2] <= nums[3]....
# There may have multiple answers for a question, you only need to consider one of the possibilities.
# Link: https://www.lintcode.com/problem/508/

class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """
    def wiggle_sort(self, nums: list[int]):
        # write your code here
        for i in range(1,len(nums)):
            if (i % 2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums
        
        



sol = Solution()
input = [1, 2, 3, 4]
ExpectedOutput =  [1, 3, 2, 4]
Output = sol.wiggle_sort(input) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(1)\n" )