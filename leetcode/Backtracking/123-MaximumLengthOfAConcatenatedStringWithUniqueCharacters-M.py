from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isUnique(t, s):
            charSet = set()
            for c in s:
                if c in t or c in charSet:
                    return False
                charSet.add(c)
            return True
        
        def backtrack(i, curr):
            if i == len(arr):
                return len(curr)
            res = 0
            # combined arr[i]
            if isUnique(curr, arr[i]):
                combinedStr = curr + arr[i]
                res = backtrack(i+1, combinedStr)
            # do not combine arr[i]
            return max(res, backtrack(i+1, curr))

        return backtrack(0, "")
    
sol = Solution()
arr = ["cha","r","act","ers"]
ExpectedOutput = 6
Output = sol.maxLength(arr)
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(m * 2^n) n for adding ele in res\n" )
