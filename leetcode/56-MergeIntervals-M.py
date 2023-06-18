class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i : i[0])
        res = []
        newInterval = intervals[0]
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                newInterval = interval
            else: 
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        res.append(newInterval)
            
        return res


sol = Solution()
intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
ExpectedOutput = [[1,3],[4,7]]
Output = sol.merge(intervals) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n Log n)\n" )
