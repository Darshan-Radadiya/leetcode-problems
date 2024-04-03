from typing import List
import heapq
from collections import deque, defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # ref: # https://medium.com/@satyem77/task-scheduler-leetcode-39d579f3440
        freq = defaultdict(int)
        maxFreq = 1
        mostFreqTasks = 0
        for t in tasks:
            freq[t] += 1
            maxFreq = max(maxFreq, freq[t])
        for t in freq:
            if freq[t] == maxFreq :
                mostFreqTasks+=1
        return max(((n+1)*(maxFreq-1)+mostFreqTasks), len(tasks))

        # 2nd approach using MaxHeap
        # step 1:- find freq. 
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1

        # Step 2 - create max heap
        maxHeap = [-freq[count] for count in freq]
        heapq.heapify(maxHeap)

        # Step 3 - queue for storing tasks that we started and its waiting to start this task again after waiting Time is over.
        q = deque() # [count, waitingTime]

        # Step 4 - process the tasks from maxHeap and queue.
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time 


sol = Solution()
tasks = ["A","A","A", "B","B","B"]
n = 3
ExpectedOutput = 10
Output = sol.leastInterval(tasks, n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n)\n" )