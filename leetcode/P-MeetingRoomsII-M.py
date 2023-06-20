
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: list[int]) -> int:
        # Write your code here
        intervals.sort(key = lambda i : i[0])
        previousMeet = intervals[0]
        room = 1
        for i in range(1,len(intervals)):
            if intervals[i][0] < previousMeet[1]:
                room += 1
            previousMeet = intervals[i]
        return room



sol = Solution()
intervals = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
ExpectedOutput = 1

intervals = [(0,30),(5,10),(15,20)]
ExpectedOutput = 2

Output = sol.min_meeting_rooms(intervals) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n Log n)\n" )