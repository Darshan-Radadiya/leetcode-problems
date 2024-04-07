from typing import List
import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = []
        for n2, n1 in zip(nums2, nums1):
            pairs.append((n2, n1))
        pairs.sort(reverse=True)
        
        minHeap = []
        n1Sum = 0
        res = 0
        for n2, n1 in pairs:
            heapq.heappush(minHeap, n1)
            n1Sum += n1
            if len(minHeap) == k:
                res = max(res, n1Sum * n2)
                poppedEle = heapq.heappop(minHeap)
                n1Sum -= poppedEle
        return res
        
        
sol = Solution()
nums1 = [2,1,14,12]
nums2 = [11,7,13,6]
k = 3
ExpectedOutput = 168
Output = sol.maxScore(nums1, nums2, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n + n log k == n log n)\n" )


        