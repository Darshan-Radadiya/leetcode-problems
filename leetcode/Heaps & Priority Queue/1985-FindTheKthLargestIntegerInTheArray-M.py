from typing import List
import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = []
        for n in nums:
            heapq.heappush(maxHeap, int(n))
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return str(maxHeap[0])
    
    
sol = Solution()
nums = ["3","6","7","10"]
k = 4
ExpectedOutput = "3"
Output = sol.kthLargestNumber(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log k) and Space is O(k)\n" )
