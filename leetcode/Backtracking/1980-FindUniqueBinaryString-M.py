from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
    # recursive solution O(n^2)
        def backtrack(i, curr):
            if i == len(nums):
                res = "".join(curr)
                return res if res not in numSet else None
            
            res = backtrack(i+1, curr)
            if res: return res

            curr[i] = "1"
            res = backtrack(i+1, curr)
            if res: return res

        numSet = {n for n in nums}
        curr = ["0" for n in nums]
        return backtrack(0, curr)
    
    
    #  Cantor's diagonal argument O(n)
        res = []
        curr = ""
        for i in range(len(nums)):
            if nums[i][i] == "1":
                curr = "0"
            else:
                curr = "1" 
            res.append(curr)

        return "".join(res)
   
    # binary to decimal O(n)

        decimal = []
        for binaryString in nums:
            decimal.append(int(binaryString, 2))

        for i in range(len(nums)+1):  
            if i not in decimal:
                res = i
                break
        res = bin(res)
        return (len(nums[0]) - len(res) + 2) * '0' + res[2:]
    
nums = ["111","011","001"]
sol = Solution()
Output = sol.findDifferentBinaryString(nums)
ExpectedOutput = "000"
# Explanation: "000" does not appear in nums. "101", "010", "100", and "110" would also be correct.
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n * 2^n) n for adding ele in res and checking palindrome\n" )
