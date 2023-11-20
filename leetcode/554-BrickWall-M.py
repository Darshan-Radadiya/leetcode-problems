class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        gapMap = {0:0}
        n = len(wall)
        for r in wall:
            gap = 0
            for j in r[:-1]:
                gap += j
                gapMap[gap] = 1 + gapMap.get(gap,0)
        print(gapMap)
        
        return n - max(gapMap.values())


sol = Solution()
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
ExpectedOutput = 2
Output = sol.leastBricks(wall) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(n)\n" )
