from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # O(n log n) 
        yearToPopulationMap = {}
        for l in logs:
            bornYear, dieYear = l[0], l[1]
            if bornYear in yearToPopulationMap:
                yearToPopulationMap[bornYear] += 1
            else:
                yearToPopulationMap[bornYear] = 1
            if dieYear in yearToPopulationMap:
                yearToPopulationMap[dieYear] -= 1
            else:
                yearToPopulationMap[dieYear] = -1
        resYear = 0
        maxPopulation = 0
        currPopulation = 0
        for year in sorted(yearToPopulationMap):
            currPopulation += yearToPopulationMap[year]
            if currPopulation > maxPopulation:
                maxPopulation = currPopulation
                resYear = year
        return resYear
            

sol = Solution()
logs = [[1950,1961],[1960,1971],[1970,1981]]
ExpectedOutput = 1960
Output = sol.maximumPopulation(logs) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n)\n" )
