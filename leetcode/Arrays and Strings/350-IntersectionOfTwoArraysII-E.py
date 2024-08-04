from typing import List
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        countOfNums1 = defaultdict(int)
        for ele in nums1:
            countOfNums1[ele] = 1 + countOfNums1.get(ele, 0)
        res = []
        for ele in nums2:
            if countOfNums1[ele] != 0:
                res.append(ele)
                countOfNums1[ele] -= 1
        return res

sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
ExpectedOutput = [9, 4]
Output = sol.intersect(nums1, nums2) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
