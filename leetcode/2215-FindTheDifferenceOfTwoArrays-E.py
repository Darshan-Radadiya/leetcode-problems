class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans1, ans2 = set(),set()
        
        for n in set(nums1):
            if n not in nums2:
                ans1.add(n)
        
        for n in set(nums2):
            if n not in nums1:
                ans2.add(n)
        return [list(ans1),list(ans2)]

sol = Solution() 
nums1 = [-68,-80,-19,-94,82,21,-43]
nums2 = [-63]
ExpectedOutput = [[-94, -19, -80, 82, 21, -43, -68], [-63]]
Output = sol.findDifference(nums1, nums2) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )