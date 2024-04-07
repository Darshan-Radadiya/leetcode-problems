from typing import List
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = []
        for e, s in zip(efficiency, speed):
            pairs.append((e, s))
        pairs.sort(reverse=True)

        speedSum = 0
        res = 0
        minHeap = []
        for e, s in pairs:
            heapq.heappush(minHeap, s)
            speedSum += s
            res = max(res, speedSum * e)
            if len(minHeap) == k:
                pops = heapq.heappop(minHeap)
                speedSum -= pops
        return res % (10 ** 9 + 7)
        
sol = Solution()
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 3
ExpectedOutput = 168
Output = sol.maxPerformance(n, speed, efficiency, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n + n log k == n log n)\n" )


        