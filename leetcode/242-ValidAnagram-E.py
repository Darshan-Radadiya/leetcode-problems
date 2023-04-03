class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countOfLetterInS = {}
        countOfLetterInT = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countOfLetterInS[s[i]] = 1 +countOfLetterInS.get(s[i], 0)
            countOfLetterInT[t[i]] = 1 + countOfLetterInT.get(t[i], 0)
        
        return countOfLetterInS == countOfLetterInT


sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))