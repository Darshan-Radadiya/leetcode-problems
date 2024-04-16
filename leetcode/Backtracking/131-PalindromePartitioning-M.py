from typing import List
class Solution:
    def palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def backtrack(self, idx, s, currSubStrs, res):
        if idx == len(s):
            res.append(currSubStrs.copy())
            return
        for i in range(idx, len(s)):
            if self.palindrome(s, idx, i):
                currSubStrs.append(s[idx:i+1])
                self.backtrack(i+1, s, currSubStrs, res)
                currSubStrs.pop()

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack(0, s, [], res)
        return res
    
s = "abbab"
sol = Solution()
Output = sol.partition(s)
ExpectedOutput = [['a', 'b', 'b', 'a', 'b'], ['a', 'b', 'bab'], ['a', 'bb', 'a', 'b'], ['abba', 'b']] 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n * 2^n) n for adding ele in res and checking palindrome\n" )
