class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        smoothImg = [[0] * len(img[0]) for _ in range(len(img))]
        ROWS = len(img)
        COLS = len(img[0])
        for r in range(ROWS):
            for c in range(COLS):
                total_sum = 0
                count = 0

                for x in range(max(0, r-1), min(ROWS, r+2)):
                    for y in range(max(0, c-1), min(COLS, c+2)):
                        total_sum += img[x][y]
                        count += 1

                smoothImg[r][c] = total_sum // count

        return smoothImg

sol = Solution()
img = [[100,200,100],[200,50,200],[100,200,100]]
ExpectedOutput = [[137,141,137],[141,138,141],[137,141,137]]
Output = sol.imageSmoother(img) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(n)\n" )
