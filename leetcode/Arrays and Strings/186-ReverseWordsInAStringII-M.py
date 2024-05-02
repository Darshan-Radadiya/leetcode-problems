from typing import List
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the whole string then 
        #  reverse the each word in reversed string. 
        def reverseWord(l, r):
        
            while l < r:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
                
        l, r = 0, len(s) - 1
        reverseWord(l, r)
        start, end = 0, 0
        while start < len(s):
            while end < len(s) and s[end] != " ":
                end += 1
            reverseWord(start, end - 1)
            start = end + 1
            end += 1
        
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
ExpectedOutput = ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
sol = Solution()
Output = sol.reverseWords(s) 
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is:O(N) and Space is O(1)\n" )
