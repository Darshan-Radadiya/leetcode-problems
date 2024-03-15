class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        finder = nums[0]
        while finder != slow:
            slow = nums[slow]
            finder = nums[finder]
        return finder


sol = Solution()
nums = [3,1,3,4,2]
ExpectedOutput = 3
Output = sol.findDuplicate(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n) \n" )

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# This problem (reportedly) took CS legend Don Knuth twenty-four hours to solve
#
# proving that at least one duplicate element
# must exist - is a straightforward application of the pigeonhole principle.
# If the values range from 0 to n - 2, inclusive, then there are only n - 1
# different values.  If we have an array of n elements, one must necessarily be
# duplicated.
#
# Can you solve the problem in linear runtime complexity?
# we can do it using the Floyd's algorithm AKS Tortoise and Hare Algorithm

# Ref:- https://keithschwarz.com/interesting/code/?dir=find-duplicate
        