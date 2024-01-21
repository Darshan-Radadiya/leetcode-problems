class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        l, r, currRes, res = 0, 0, 0, 0
        vowels = "aeiou"
        # currWindow = []

        while r < len(s):
            if (r - l) < k:
                # currWindow.append(s[r])
                if s[r] in vowels:
                    currRes += 1
                r += 1
            else:
                if s[l] in vowels:
                    currRes -= 1
                # currWindow.remove(s[l])
                l += 1
            res = max(res, currRes)
        return res
    
s = "abciiidef"
k = 3
ExpectedOutput = 3
sol = Solution()
Output = sol.maxVowels(s, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )

