class Solution:
    def lengthOfLongestSubstring(self, s):
        longSubS = ""
        res = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    

sol = Solution()
s = "abcabcbb"
# s = "pwwkew"
# s ="bbbb"
Output = 3
print("Expected Output:", Output)
print("Output: ", sol.lengthOfLongestSubstring(s))