from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        prev_end = points[0][1]
        res = 1
        for start, end in points:
            if prev_end < start:
                res += 1
                prev_end = end 
        return res

sol = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
ExpectedOutput = 2
Output = sol.findMinArrowShots(points) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n Log n)\n" )
