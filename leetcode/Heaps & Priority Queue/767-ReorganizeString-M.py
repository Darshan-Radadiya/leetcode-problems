import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freqS = {}
        for c in s:
            if c not in freqS:
                freqS[c] = 0
            freqS[c] += 1
        maxHeap = []
        for c, freq in freqS.items():
            heapq.heappush(maxHeap, (-freq, c))  
        res = ""
        while len(maxHeap) > 1:
            negFreq1, char1 = heapq.heappop(maxHeap)  
            negFreq2, char2 = heapq.heappop(maxHeap)  
            res += char1 + char2
            
            if negFreq1 < -1:  
                heapq.heappush(maxHeap, (negFreq1 + 1, char1))
            if negFreq2 < -1:  
                heapq.heappush(maxHeap, (negFreq2 + 1, char2))
        
        if maxHeap: 
            negFreq, char = maxHeap[0]
            if -negFreq > 1: 
                return ""
            res += char 
        
        return res


sol = Solution()
s = "vvvlo"
ExpectedOutput = "vlvov"
Output = sol.reorganizeString(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O( n + n log k == n log n) and Space is O(n) + O(k) == O(n)\n" )