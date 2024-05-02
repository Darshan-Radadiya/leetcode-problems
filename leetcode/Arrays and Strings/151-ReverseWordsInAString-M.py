class Solution:
    def reverseWords(self, s: str) -> str:
        wordStack = []
        i = 0
        n = len(s)
        while i < n:
            while i < n and s[i] == ' ':  # Skip spaces
                i += 1
            start = i
            while i < n and s[i] != ' ':  # Find the end of the current word
                i += 1
            if start < i:  # If a word has been found
                wordStack.append(s[start:i])

        res = ""
        while wordStack:
            res += wordStack.pop()
            if wordStack:
                res += " "
        return res

s = "  hello world  "
ExpectedOutput = "world hello"
sol = Solution()
Output = sol.reverseWords(s) 
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is:O(N)\n" )
