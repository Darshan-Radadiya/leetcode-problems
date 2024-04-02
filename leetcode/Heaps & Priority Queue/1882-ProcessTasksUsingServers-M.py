from typing import List
import heapq
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)
        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)

        unavailable = []
        currTime = 0
        for i in range(len(tasks)):
            currTime = max(currTime, i)
            if len(available) == 0:
                currTime = unavailable[0][0]
            while unavailable and currTime >= unavailable[0][0]:
                freeTime, weight, idx = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, idx))
             
            weight, idx = heapq.heappop(available)
            res[i] = idx
            heapq.heappush(unavailable, (currTime + tasks[i], weight, idx))
        return res
    
sol = Solution()
servers = [5,1,4,3,2]
tasks = [2,1,2,4,5,2,1]
ExpectedOutput = [1,4,1,4,1,3,2]
Output = sol.assignTasks(servers, tasks) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O( m + log m + m log n == m log n) and Space is O(n) + O(m) == O(n)\n" )
