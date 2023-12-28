class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        i, res = 0,  []
        currLine, currLineLength = [], 0

        while i < len(words):

            if (len(currLine) + currLineLength + len(words[i])) > maxWidth:
                extraSpace = maxWidth - currLineLength
                spacePerWord = extraSpace // max(1, len(currLine) - 1)
                reminderSpacePerWord = extraSpace % max(1, len(currLine) - 1)

                for j in range(max(1, len(currLine) - 1)):
                    currLine[j] += " " * spacePerWord
                    if reminderSpacePerWord:
                        currLine[j] += " " 
                        reminderSpacePerWord -= 1
                
                res.append("".join(currLine))
                currLine, currLineLength = [], 0

            currLine.append(words[i])
            currLineLength += len(words[i])
            i += 1

        lastLine = " ".join(currLine)
        trailSpace = maxWidth - len(lastLine)
        res.append(lastLine + " " * trailSpace)
        
        return res
        

sol = Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
ExpectedOutput = [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
Output = sol.fullJustify(words, maxWidth) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
