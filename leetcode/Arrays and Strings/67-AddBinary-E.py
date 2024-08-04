class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aLen = len(a)
        bLen = len(b)
        aR, bR = aLen-1, bLen-1
        res = ""
        carry = "0"
        while aR >= 0 or bR >= 0:
            currB = 0 if bR < 0 else b[bR]
            currA = 0 if aR < 0 else a[aR]
            
            if currA == "1" and currB == "1" and carry == "1":
                res = "1" + res
                carry = "1"
            elif (currA == "1" and currB =="1") or (currA == "1" and carry == "1") or (currB == "1" and carry == "1"):
                res = "0" + res
                carry = "1"
            elif currA == "1" or currB == "1" or carry == "1":
                res = "1" + res
                carry = "0"
            else:
                res = "0" + res
                carry = "0"
            aR -= 1
            bR -= 1
        if carry == "1": res = "1" + res
        return res
            
sol = Solution() 
a = "10100101"
b = "1011"
ExpectedOutput = "10110000" 
Output = sol.addBinary(a, b) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(max(m,n))\n" )
