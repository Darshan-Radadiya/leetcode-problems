class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        n = len(s)
        res = ""
        while i < n:
            while i < n and s[i] == ' ':  # Skip spaces
                i += 1
            start = i
            while i < n and s[i] != ' ':  # Find the end of the current word
                i += 1
            if start < i:  # If a word has been found
                currWord = s[start:i]
                res += currWord[::-1] + " "
        
        return res[:len(res)-1]
        
sol = Solution()
s = "Let's take LeetCode contest"
ExpectedOutput = "s'teL ekat edoCteeL tsetnoc"
Output = sol.reverseWords(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(n)\n" )
