class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)

        if s == "":
            return True
        elif sLen <= tLen:
            sPointer, tPointer = 0, 0
            while tPointer < tLen and sPointer < sLen:
                if s[sPointer] == t[tPointer]:
                    sPointer += 1
                    tPointer += 1
                else:
                    tPointer += 1
        else:
            return False

        return sPointer == sLen



sol = Solution()

# True
# s = "abc"
# t = "ahbgdc"

# False
s = "axc"
t = "ahbgdc"

ExpectedOutput = False
Output = sol.isSubsequence(s,t) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n). Here n is length of T.\n" )
