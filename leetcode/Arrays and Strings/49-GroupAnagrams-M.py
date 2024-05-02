# Time complexity = O(m*n*26) but we can neglect constant so its O(m*n)
 
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqToWordsMap = {} # [0]*26 : [ list of words]
        
        def wordToFreq(word):
            freq = [0]*27
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            return freq
        for word in strs:
            getFreqOfWord = wordToFreq(word)
            if tuple(getFreqOfWord) in freqToWordsMap:
                freqToWordsMap[tuple(getFreqOfWord)].append(word)
            else:
                freqToWordsMap[tuple(getFreqOfWord)] = []
                freqToWordsMap[tuple(getFreqOfWord)].append(word)
        res = []
        for freqMap in freqToWordsMap:
            res.append(freqToWordsMap[freqMap])
        return res

sol = Solution()
ExpectedOutput = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
Output = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(m*n*26) == O(m*n)\n" )
