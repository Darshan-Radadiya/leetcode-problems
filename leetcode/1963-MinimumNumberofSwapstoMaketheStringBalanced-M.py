class Solution:
    def minSwaps(self, s: str) -> int:

        end = len(s) - 1
        extraCLosingBracket = 0
        ans = 0
        i = 0
        for i in range(end):
            if s[i] == ']':
                extraCLosingBracket += 1
                ans = max(extraCLosingBracket, ans)
            else:
                extraCLosingBracket -= 1
        
        return (ans+1) // 2
            
sol = Solution()
s = "]]][[["
ExpectedOutput = 2
Output = sol.minSwaps(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(1)\n" )
