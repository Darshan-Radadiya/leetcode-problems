class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l1, l2 = len(nums1), len(nums2)
        l, r = 0, l1
        while l <= r:
            partitionNums1 = l + ((r - l) // 2)
            partitionNums2 = ((l1 + l2 + 1) // 2) - partitionNums1

            nums1Left  = nums1[partitionNums1 - 1] if partitionNums1 - 1 >= 0 else float('-inf')
            nums1Right = nums1[partitionNums1] if partitionNums1 < l1 else float('inf')

            nums2Left  = nums2[partitionNums2 - 1] if partitionNums2 - 1 >= 0 else float('-inf')
            nums2Right = nums2[partitionNums2] if partitionNums2 < l2 else float('inf')

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if (l1+l2) % 2 == 0:
                    # even len
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
                else:
                    # odd len
                    return max(nums1Left, nums2Left)

            elif nums1Left > nums2Right:
                r = partitionNums1 - 1
            else:
                l = partitionNums1 + 1
    
sol = Solution()
a1 = [1,2,3,7]   
a2 = [3,4,5,6]
ExpectedOutput = 3.5
Output = sol.findMedianSortedArrays(a1, a2) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(Log(m+n))\n" )
