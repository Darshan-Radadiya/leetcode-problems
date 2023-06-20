class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: list[int]) -> bool:
        intervals.sort(key = lambda i : i[0])
        previousMeet = intervals[0]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] < previousMeet[1]:
                return False
            previousMeet = intervals[i]
        return True
        

sol = Solution()
intervals = [(0,30),(5,10),(15,20)]
ExpectedOutput = False
Output = sol.can_attend_meetings(intervals) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n Log n)\n" )
