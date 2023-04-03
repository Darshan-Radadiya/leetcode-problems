# Time complexity = O(m*n*26) but we can neglect constant so its O(m*n)
 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        if len(strs) == 1:
            return [strs]
        hashMap = defaultdict(list)
        for i in range(len(strs)):
            numberOfLetter = [0]*27
            for letter in strs[i]:
                numberOfLetter[ord(letter)-96] += 1
                # we can use this as well.
                # numberOfLetter[ord(letter)-ord("a")] = numberOfLetter[ord(letter)-ord("a")] + 1
            hashMap[tuple(numberOfLetter)].append(strs[i])
        return hashMap.values()

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
