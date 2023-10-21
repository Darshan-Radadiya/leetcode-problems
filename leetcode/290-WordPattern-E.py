class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:   
        s = s.split()
        if len(set(pattern)) != len(set(s)):
            return False
        if len(pattern) != len(s):
            return False
            
        wordMap = {}
        for i in range(len(s)):
            if pattern[i] not in wordMap:
                wordMap[pattern[i]] = s[i]
            elif wordMap[pattern[i]] == s[i]:
                continue
            else:
                return False
        return True





sol = Solution()
pattern = "abba"
s = "dog cat cat dog"
Output = True
ExpectedOutput = True
Output = sol.wordPattern(pattern, s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
