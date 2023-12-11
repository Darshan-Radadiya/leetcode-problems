class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < 2**k:
            return False
        else:
            binarySet = set()
            for i in range((len(s) - k)+1):
                if s[i:i+k] not in binarySet:
                    binarySet.add(s[i:i+k])            
        return True if len(binarySet) == 2**k else False



sol = Solution()
s = "011100"
k = 2
ExpectedOutput = True
Output = sol.hasAllCodes(s,k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )
