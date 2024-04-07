from typing import List
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks[i] = [enqueue Time, processing Time]
        tasks.sort()

        for i in range(len(tasks)):
            tasks[i].append(i)
        res = []
        minHeap = []
        i = 0
        time = 0

        while i < len(tasks) or minHeap:
            # Add the tasks in the minHeap queue
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            if minHeap:
                processingTime, index = heapq.heappop(minHeap)
                res.append(index)
                time += processingTime
            else:
                time = tasks[i][0]
        return res
sol = Solution()
tasks = [[1,2],[2,4],[3,2],[4,1]]
ExpectedOutput = [0,2,3,1]
Output = sol.getOrder(tasks) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n)\n" )


        