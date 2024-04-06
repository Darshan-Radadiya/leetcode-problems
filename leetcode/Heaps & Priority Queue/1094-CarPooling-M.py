import heapq 
from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    #    O(n)
        location = [0] * 1001
        for p, s, e in trips:
            location[s] += p
            location[e] -= p
        currPass = 0
        for l in location:
            currPass += l
            if currPass > capacity:
                return False
        return True

    #    O( n log n)
        trips.sort(key = lambda f:f[1])
        minHeap = []
        currPass = 0
        for p, f, t in trips:
            while minHeap and minHeap[0][0] <= f:
                currPass -= minHeap[0][1]
                heapq.heappop(minHeap)
                
            currPass += p
            if currPass > capacity:
                return False
            heapq.heappush(minHeap, (t, p))
        return True
    
sol = Solution()
trips = [[2,1,5],[3,3,7]]
capacity = 5
ExpectedOutput = True
Output = sol.carPooling(trips, capacity) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n) and Space is O(k)\n" )
