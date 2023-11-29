class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, len(needle)
        while r <= len(haystack): 
            print( haystack[l:r])
            if haystack[l:r] == needle:
                return l
            else:
                l += 1
                r += 1
        return -1

sol = Solution()
s = "sadcumsad"
p = "sad"
ExpectedOutput = 2
Output = sol.strStr(s, p) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n*m) and Space Complexity is O(1)\n" )