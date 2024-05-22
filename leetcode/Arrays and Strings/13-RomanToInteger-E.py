class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I":1, "II":2, "IV":4, "V":5, "IX":9, "X": 10, "XL":40, "L":50, "XC":90,
        "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        i = 0
        res = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] in ["I", "X", "C"] and s[i] + s[i+1] in map:
                combined_num = s[i] + s[i+1]
                res += map[combined_num]
                i += 2
            else:
                res += map[s[i]]
                i += 1
        return res
                

sol = Solution()
s = "MCMXCIV"
ExpectedOutput = 1994
Output = sol.romanToInt(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(1) \n" )
