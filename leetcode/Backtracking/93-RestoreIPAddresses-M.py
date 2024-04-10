from typing import List
class Solution:
    def backtrack(self, i, parts, curr, res):
        if i == len(s) and parts == 4:
            res.append(curr[:-1])
            return
        if parts > 4:
            return
        for j in range(i, min(len(s), i+3)):
            if int(s[i : j+1]) < 256 and (i == j or s[i] != "0"):
                self.backtrack(j+1, parts + 1, curr + s[i : j+1] + ".", res)

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []
        self.backtrack(0, 0, "", res)
        return res



s = "25525511135"
sol = Solution()
Output = sol.restoreIpAddresses(s)
ExpectedOutput = ["255.255.11.135","255.255.111.35"]
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n * 3^4) n for adding ele in res\n" )
