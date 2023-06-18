class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        res = 0
        intervals.sort(key = lambda i : i[0])

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else: 
                res += 1
                prevEnd = min(end, prevEnd)
        return res
        


sol = Solution()
intervalsS = [ [[1,2],[2,3],[3,4],[1,3]],    [[1,2],[1,2],[1,2]],   [[1,2],[2,3]] ]
ExpectedOutputS = [ 1, 2, 0 ]

for intervals, ExpectedOutput in zip(intervalsS, ExpectedOutputS):
    Output = sol.eraseOverlapIntervals(intervals) 
    print("\nOutput is:      ", Output ,"\n" )
    print("Expected Output:",ExpectedOutput,"\n" )
    print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("\tTime Complexity is: O(n Log n) '\033[1m' log n for sorting '\033[0m'and  '\033[1m'n for iterating over intervals '\033[0m'\n" )
