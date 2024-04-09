from typing import List
class Solution:
    def backtrack(self,i, keyboard, digits, res, curr):
        if len(curr) == len(digits):
            res.append(curr)
            return
        for ch in keyboard[digits[i]]:
            self.backtrack(i+1, keyboard, digits, res, curr + ch)
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return ""
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        res = []
        self.backtrack(0, keyboard, digits, res, "")
        return res
    
    
nums = "25"
sol = Solution()
Output = sol.letterCombinations(nums)
ExpectedOutput = ['aj', 'ak', 'al', 'bj', 'bk', 'bl', 'cj', 'ck', 'cl'] 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n * 2^n) n for adding ele in res\n" )
