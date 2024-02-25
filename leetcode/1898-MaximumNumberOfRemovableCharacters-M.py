class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def isSubsequence(s, subSequence, removed):
            i, j = 0 , 0
            while i < len(s) and j < len(subSequence):
                if i not in removed and s[i] == subSequence[j]:
                    j += 1
                i += 1
            return j == len(subSequence)

        res = 0
        l, r = 0, len(removable) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            removed = set(removable[:mid+1])
            if isSubsequence(s, p, removed):
                res = max(res, mid + 1)
                l = mid + 1
            else:
                r = mid - 1
        return res

sol = Solution()
s = "abcacb"
p = "ab"
removable = [3,1,0]
ExpectedOutput = 2
Output = sol.maximumRemovals(s, p , removable) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n log k)\n" )
