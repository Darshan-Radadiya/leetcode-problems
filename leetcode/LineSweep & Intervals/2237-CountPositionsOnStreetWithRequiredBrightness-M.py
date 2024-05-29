from typing import List
from collections import defaultdict
class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        line = defaultdict(int)
        for start, end in lights:
            line[max(0, start - end)] += 1
            line[min(n-1, start + end) + 1] -= 1
        res, total = 0, 0
        for i in range(n):
            total += line[i]
            if total >= requirement[i]:
                res += 1
        return res


sol = Solution()
n = 5
lights = [[0,1],[2,1],[3,2]]
requirement = [0,2,1,4,1]
ExpectedOutput = 4
Output = sol.meetRequirement(n, lights, requirement) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
