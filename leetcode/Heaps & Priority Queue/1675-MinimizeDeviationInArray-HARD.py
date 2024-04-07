from typing import List
import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxEle = float("-inf")
        minEle = float("inf")
        maxHeap = []
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums[i] *= 2
            nums[i] *= -1
            maxEle = max(maxEle, -nums[i])
            minEle = min(minEle, -nums[i])
            heapq.heappush(maxHeap, nums[i])
        res = maxEle - minEle

        while maxHeap[0] % 2 == 0:
            currMax = -heapq.heappop(maxHeap)
            res = min(res, currMax - minEle)
            currMax //= 2
            minEle = min(minEle, currMax)
            heapq.heappush(maxHeap, -currMax)
            
        res = min(res, -heapq.heappop(maxHeap) - minEle)
        return res

sol = Solution()
nums = [4,1,5,20,3]
ExpectedOutput = 3
Output = sol.minimumDeviation(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log m * log n)\n" )


        