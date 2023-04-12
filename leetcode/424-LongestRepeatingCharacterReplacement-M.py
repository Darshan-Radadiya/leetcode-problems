class Solution:
    def characterReplacement(self, s, k):
        freq = {}
        res = 0
        l = 0
        currentWindowSize = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r],0)
            currentWindowSize = r - l + 1
            if currentWindowSize - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, currentWindowSize)
        
        return res
                 


        




sol = Solution()
s = "ABAB"
k = 2
Output = 4
print("Expected Output:", Output)
print("Output: ", sol.characterReplacement(s,k))