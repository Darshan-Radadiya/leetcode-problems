class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #pair of character and its count
        res = ""
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                stack.pop()
        for char, count in stack:
            res += (char * count)
        return res

s = "pbbcggttciiippooaais"
k = 2
ExpectedOutput = "ps"
sol = Solution()
Output = sol.removeDuplicates(s,k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )

