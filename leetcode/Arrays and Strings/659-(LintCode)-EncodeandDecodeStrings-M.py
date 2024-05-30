# link - https://www.lintcode.com/problem/659/

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        listToStr = ""
        for word in strs:
            listToStr += str(len(word)) + "#" + (str(word))
        return listToStr

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1: j+1+length])
            i = j + length + 1
        return res

sol = Solution()
original_input = ['lint','4#code','2#lo2#ve','you']
input = sol.encode(original_input)
output = sol.decode(input)
if original_input == output:
    print( "Successfully encoded and decoded... :)")
else:
    print("Failed...Try Again..")