
from typing import List 
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [[9,10],[4,9],[4,17]]
        startTime = sorted(t[0] for t in intervals)
        endTime = sorted(t[1] for t in intervals)
        # startTime = 4, 4, 9 
        # endTime = 9, 10, 17
        j = 0
        res = 0
        for i in range(len(startTime)):
            if startTime[i] >= endTime[j]:
                j += 1
            else:
                res += 1
        return res


sol = Solution()
intervals = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
ExpectedOutput = 1

intervals = [(0,30),(5,10),(15,20)]
ExpectedOutput = 2

Output = sol.minMeetingRooms(intervals) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n Log n)\n" )