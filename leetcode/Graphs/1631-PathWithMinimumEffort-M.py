import heapq
from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = []
        ROWS = len(heights)
        COLS = len(heights[0])
        res = [[float("inf")] * COLS for _ in range(ROWS)]
        heapq.heappush(pq, (0, 0, 0)) # diff, r, c
        res[0][0] = 0
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        while pq:
            diff, r, c = heapq.heappop(pq)
            # Because there is no way that the rest of elements can update the weight of 
            # des cell even smaller due to the min heap.
            if(r == ROWS - 1 and c == COLS - 1):
                return diff
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if min(nr,nc) < 0 or nc == COLS or nr == ROWS or diff > res[nr][nc]:
                    continue
                absDiff = max(diff, abs(heights[r][c] - heights[nr][nc] ))
                if res[nr][nc] > absDiff:
                    res[nr][nc] =  absDiff
                    heapq.heappush(pq, (absDiff, nr, nc))
        return res[ROWS-1][COLS-1]
    
heights = [[1,2,2],[3,8,2],[5,3,5]]
sol = Solution()
Output = sol.minimumEffortPath(heights)
ExpectedOutput = 2
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(N^2) and Space O(N)\n" )