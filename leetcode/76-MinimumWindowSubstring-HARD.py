#Airbnb
class Solution:
    def minWindow(self, s, t):

        if t == "": 
            return ""
        
        freqT = {}
        freqWindowS = {}

        for i in range(len(t)):
            freqT[t[i]] = 1 + freqT.get(t[i],0)
        
        resLen = float("infinity")
        res = [-1, -1]
        l = 0
        have, need = 0, len(freqT)

        for r in range(len(s)):
            freqWindowS[s[r]] = 1 + freqWindowS.get(s[r], 0)

            # incrementing have count.
            if s[r] in freqT and freqWindowS[s[r]] == freqT[s[r]]:
                have += 1

            while have == need:
                # updating the res.
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # to pop the ele from left
                freqWindowS[s[l]] -= 1
                if s[l] in freqT and freqWindowS[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+1] if resLen != float("infinity") else ""

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
Output = "BANC"
print("Expected Output:", Output)
print("Output: ", sol.minWindow(s,t))