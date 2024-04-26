from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charIdx = {c : i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j > len(w2)-1:
                    return False
                if charIdx[w1[j]] > charIdx[w2[j]]:
                    return False
                if charIdx[w1[j]] != charIdx[w2[j]]:
                    break
        return True

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
sol = Solution()
Output = sol.isAlienSorted(words, order)
ExpectedOutput = True
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(N + M) n is len of order and M is no. of char in words.\n" )