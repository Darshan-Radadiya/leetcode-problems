class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMapT = {}
        tMapS = {}

        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            if (charS in sMapT and sMapT[charS] != charT or charT in tMapS and tMapS[charT] != charS):
                return False
            sMapT[charS] = charT
            tMapS[charT] = charS

        return True



sol = Solution()
s = "bbbaaaba"
t = "aaabbbba"
ExpectedOutput = False
Output = sol.isIsomorphic(s,t) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
