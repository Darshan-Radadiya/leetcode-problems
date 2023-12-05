class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        prevSubStr = set()
        # hashMap = {}
        ans = set()
        # ans = []
        for i in range(len(s)-9):
            # if len(s) - i >= 10:
            #     currSubStr = ''
            #     for j in range(i, i+10):
            #         currSubStr += s[j]
            currSubStr = s[i:i+10]
            if currSubStr in prevSubStr:
                ans.add(currSubStr)
            else:
                prevSubStr.add(currSubStr)
        
        # ans = [val for val in hashMap if hashMap[val] >=2]            
        return list(ans)


sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
ExpectedOutput = ['AAAAACCCCC', 'CCCCCAAAAA']
Output = sol.findRepeatedDnaSequences(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )
