from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclideanDist = []
        heapq.heapify(euclideanDist)
        for xy in points:
            ed = ((xy[0] - 0)**2) + ((xy[1] - 0)**2)
            heapq.heappush(euclideanDist,[-ed, xy])
            if len(euclideanDist) > k:
                heapq.heappop(euclideanDist)
        res = []
        for xy in euclideanDist:
            res.append(xy[1])
        return res

sol = Solution()
points = [[3,3],[5,-1],[-2,4]]
k = 2
Output = sol.kClosest(points, k) 
ExpectedOutput = [[-2,4],[3,3]]
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log k) and Space is O(k)\n" )
