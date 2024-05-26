from typing import List
class Solution:
    # O(n)
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            #  no overlap then add interval as is...
            if interval[1] < toBeRemoved[0] or interval[0] > toBeRemoved[1]:
                res.append(interval)
            else:
                # is there left interval we need to keep...
                if interval[0] < toBeRemoved[0]:
                    res.append([interval[0], toBeRemoved[0]])
                # is there right interval we need to keep...
                if interval[1] > toBeRemoved[1]:
                    res.append([toBeRemoved[1], interval[1]])
        return res
            
sol = Solution()
intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]]
toBeRemoved = [-1,4]
ExpectedOutput = [[-5,-4],[-3,-2],[4,5],[8,9]]
Output = sol.removeInterval(intervals, toBeRemoved) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(n)\n" )
