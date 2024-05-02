class Solution:

    def checkPalindrome(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
            
    def longestPalindrome(self, s: str) -> str:
        palindromeStr = ""
        if s == "":
            return palindromeStr
    
        for i in range(len(s)):

            #odd length
            l, r = i, i
            tempStr = self.checkPalindrome(s,l,r)
            if len(tempStr) > len(palindromeStr):
                palindromeStr = tempStr 
                
            #Even length
            l, r = i, i+1
            tempStr = self.checkPalindrome(s,l,r)
            if len(tempStr) > len(palindromeStr):
                palindromeStr = tempStr

        return palindromeStr

sol = Solution()
s = "aaa"
ExpectedOutput = "bab"
Output = sol.longestPalindrome(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n*n) or O(n^2)\n" )
