class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lastIdx = m + n - 1
        while m > 0 and n  > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[lastIdx] = nums1[m-1]
                m -= 1
            else:
                nums1[lastIdx] = nums2[n-1]
                n -= 1
            lastIdx -= 1

        while n > 0:
            nums1[lastIdx] = nums2[n-1]
            n -= 1
            lastIdx -= 1
        return nums1

sol = Solution()
nums1 = [1,2,3,0,0,0]
m, n = 3, 3
nums2 = [2,5,6]
ExpectedOutput = [1,2,2,3,5,6]
Output = sol.merge(nums1, m, nums2, n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n + m)\n" )
