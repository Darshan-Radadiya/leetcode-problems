from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, n)
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return maxHeap[0]
    
sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
ExpectedOutput = 4
Output = sol.findKthLargest(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log k) and Space is O(k)\n" )
