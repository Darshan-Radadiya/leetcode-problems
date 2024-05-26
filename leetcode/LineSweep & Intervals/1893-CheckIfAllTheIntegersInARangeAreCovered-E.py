from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        line = [0] * 52
        for r in ranges:
            line[r[0]] += 1
            line[r[1] + 1] -= 1
        
        overlap = 0
        for i in range(1, 52):
            overlap += line[i]
            if left <= i <= right and overlap <= 0:
                return False
        return True
    
sol = Solution()
ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5
ExpectedOutput = True
Output = sol.isCovered(ranges, left, right) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
