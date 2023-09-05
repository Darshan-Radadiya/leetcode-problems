class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        heightStack = []

        for i, h in enumerate(heights):
            
            start = i
            while heightStack and heightStack[-1][1] > h:
                index, height = heightStack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            heightStack.append((start, h))
        
        for i, h in heightStack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
    



sol = Solution()
heights = [2,1,5,6,2,3]
ExpectedOutput = 10
Output = sol.largestRectangleArea(heights) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )

