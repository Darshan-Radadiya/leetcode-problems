class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        frequency = {}
        for length, width in rectangles:
            ratio = length / width
            if ratio in frequency:
                frequency[ratio] += 1
            else:
                frequency[ratio] = 1 
        pairs = 0
        print(frequency)
        for key in frequency:
            value = frequency[key]
            pairs += ((value - 1) * value) // 2
        return pairs

sol = Solution()
rectangles = [[4,8],[3,6],[10,20],[15,30]]
ExpectedOutput = 6
Output = sol.interchangeableRectangles(rectangles) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(n)\n" )
