class Solution:
    def checkPalindrome(self,s,l,r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
    def countSubstrings(self, s: str) -> int:
        palindromeStrCount = 0

        for i in range(len(s)):
            #odd length
            palindromeStrCount += self.checkPalindrome(s,i,i)
                
            #Even length
            palindromeStrCount += self.checkPalindrome(s,i,i+1)

        return palindromeStrCount

sol = Solution()
s = "aaa"
ExpectedOutput = 6
Output = sol.countSubstrings(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n*n) or O(n^2)\n" )
