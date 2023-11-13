class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        wordMap={}
        for c in text:
            wordMap[c] = 1 + wordMap.get(c, 0)
        
        count = 0
        while 'b' in wordMap and wordMap['b'] >= 1:
            for i in "balloon":
                if i in wordMap and wordMap[i] >= 1:
                    wordMap[i] -= 1 
                else:
                    return count
            count += 1
        return count

sol = Solution()
text = "loonbalxballpoon"
ExpectedOutput = 2
Output = sol.maxNumberOfBalloons(text) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
