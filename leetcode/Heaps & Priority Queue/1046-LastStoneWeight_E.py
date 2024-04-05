from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [s*-1 for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone2 != stone1:
                heapq.heappush(stones, stone1 - stone2)
        stones.append(0)
        return abs(stones[0])
    
sol = Solution()
stones = [2,7,4,1,8,1]
ExpectedOutput = 1
Output = sol.lastStoneWeight(stones) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n)\n" )
