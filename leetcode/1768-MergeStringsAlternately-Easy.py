class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        minLen = min(len(word1), len(word2))
        for i in range(minLen):
            res += word1[i] + word2[i]
    
        res += word1[minLen:]+word2[minLen:]
        return res

sol = Solution()
word1 = "abcd"
word2 = "pqfbdshjbg"
ExpectedOutput = "apbqcfdbdshjbg" 
Output = sol.mergeAlternately(word1, word2) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n)\n" )
