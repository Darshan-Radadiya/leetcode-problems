class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []

        freqP = {}
        for i in range(len(p)):
            freqP[p[i]] = 1 + freqP.get(p[i],0)
        
        l = 0
        freqS = {}

        for i in range(len(s)):
            if s[i] in freqP:
                freqS[s[i]] = 1 + freqS.get(s[i], 0)

                while freqS[s[i]] > freqP[s[i]]:
                    freqS[s[l]] -= 1
                    if freqS[s[l]] == 0:
                        del freqS[s[l]]
                    l += 1

                if freqS == freqP:
                    res.append(l)
            else:
                # Reset freqS and move l to i + 1
                freqS = {}
                l = i + 1
        return res

sol = Solution()
s = "cbaebabacd"
p = "abc"
ExpectedOutput = [0,6]
Output = sol.findAnagrams(s, p) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(n)\n" )