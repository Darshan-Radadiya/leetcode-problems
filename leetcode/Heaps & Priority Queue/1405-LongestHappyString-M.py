import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        
        while maxHeap:
            c1, char1 = heapq.heappop(maxHeap)
            # check if same char appears 2 times if so, then pop another char
            if len(res) > 1 and res[-2] == res[-1] == char1:
                if not maxHeap:
                    break
                c2, char2 = heapq.heappop(maxHeap)
                res += char2
                c2 += 1
                if c2:
                    heapq.heappush(maxHeap, (c2, char2))
            # char not appears more than 2 times so we can push it to res
            else:
                res += char1
                c1 += 1
            if c1:
                heapq.heappush(maxHeap, (c1, char1))

        return res                
sol = Solution()
a = 1
b = 1
c = 7
ExpectedOutput = "ccaccbcc"
Output = sol.longestDiverseString(a, b, c) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
            
                    