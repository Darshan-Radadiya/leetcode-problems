from collections import Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for mid in range(len(s)):
            right[s[mid]]-=1
            if right[s[mid]] == 0:
                right.pop(s[mid])
            
            for c in left:
                if c in right:
                    res.add(c+s[mid]+c)
            
            left.add(s[mid])
        
        return len(res)

 



sol = Solution()
s = "bbcbaba"
ExpectedOutput = 4
Output = sol.countPalindromicSubsequence(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(n)\n" )


