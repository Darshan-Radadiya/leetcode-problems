class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWordLen = 0
        for i in range(len(s) - 1, -1, -1):
            if (s[i] == " "):
                if lastWordLen >= 1:
                    return lastWordLen
            else:
                lastWordLen += 1
        return lastWordLen



sol = Solution()
# s = "   fly me   to   the moon  "
s = "luffy is still joyboy a hola"
ExpectedOutput = 4
Output = sol.lengthOfLastWord(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(len(lastWord))\n" )
