from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Create a dictionary to map difficulty to max profit
        ProfitToDiff = {}
        for d, p in zip(difficulty, profit):
            if d in ProfitToDiff:
                ProfitToDiff[d] = max(ProfitToDiff[d], p)
            else:
                ProfitToDiff[d] = p

        # Sort the dictionary by difficulty
        sorted_jobs = sorted(ProfitToDiff.items())
        
        # Prepare for processing the workers
        res = 0
        max_profit = 0
        j = 0

        # Sort the workers by their capacities
        worker.sort()

        for w in worker:
            # Update max_profit for the current worker capacity
            while j < len(sorted_jobs) and sorted_jobs[j][0] <= w:
                max_profit = max(max_profit, sorted_jobs[j][1])
                j += 1
            res += max_profit

        return res

sol = Solution()
difficulty = [2,17,19,20,24,29,33,43,50,51,57,67,70,72,73,75,80,82,87,90]
profit = [6,7,10,17,18,29,30,31,34,39,40,42,48,54,57,78,78,78,83,88]
worker = [12,9,11,41,11,87,48,6,48,93,76,73,7,50,55,97,47,33,46,10]
ExpectedOutput = 693
Output = sol.maxProfitAssignment(difficulty, profit, worker) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n) and O(n)\n" )
