class Solution:
    def maxProduct(self, s: str) -> int:
        ans = 0
        n = len(s)
        palindromMap = {}
        for mask in range(1, 2 ** n):
            subSeq = ""
            for i in range(n):
                if mask & (1 << i):
                    subSeq += s[i]
            if subSeq == subSeq[::-1]:
                palindromMap[mask] = len(subSeq)
        
        for mask1 in palindromMap:
            for mask2 in palindromMap:
                if mask1 & mask2 == 0:
                    ans = max(ans, palindromMap[mask1] * palindromMap[mask2])
                    
        return ans

sol = Solution()
s = "leetcodecom"
ExpectedOutput = 9
Output = sol.maxProduct(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity for worst case is: O(4^n) and Space Complexity is O(n)\n" )
