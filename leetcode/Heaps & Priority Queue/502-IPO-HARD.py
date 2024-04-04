import heapq
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitalMinHeap = []
        profitMaxHeap = []
        for c, p in zip(capital, profits):
            heapq.heappush(capitalMinHeap, (c, p))
        
        for i in range(k):
            while capitalMinHeap and capitalMinHeap[0][0] <= w:
                capital, profit = heapq.heappop(capitalMinHeap)
                heapq.heappush(profitMaxHeap, (-profit, capital))
            if not profitMaxHeap:
                break
            w += (profitMaxHeap[0][0] * -1)
            heapq.heappop(profitMaxHeap)
        return w

sol = Solution()
k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]
ExpectedOutput = 6
Output = sol.findMaximizedCapital(k, w, profits, capital) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(k log n) and Space is O(n) + O(k) == O(n)\n" )
