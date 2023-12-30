from collections import defaultdict
class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        GroupMap = defaultdict(set)
        for i in ideas:
            GroupMap[i[0]].add(i[1:])
      
        res = 0
        for i in range(ord('a'), ord('z')+1):
            for j in range(ord((chr(i)))+1, ord('z')+1):
                lenOfGrp1, lenOfGrp2 = len(GroupMap[chr(i)]), len(GroupMap[chr(j)])
                if lenOfGrp1 > 0 and lenOfGrp2 > 0:
                    for memberInI in GroupMap[chr(i)]:
                        if memberInI in GroupMap[chr(j)]:
                            lenOfGrp1 -= 1
                            lenOfGrp2 -= 1
                res += (lenOfGrp1 * lenOfGrp2 * 2)
        return res


sol = Solution()
ideas = ["aye","apple","alpha","bat","bee","bye","car", "cat", "time", "david", "donut", "zebus", "zulu", "hulu"]
# ideas = ["coffee","donuts","time","toffee"] o/p = 6
# ideas = ["aaa","baa","caa","bbb","cbb","dbb"] o/p = 2
ExpectedOutput = 142
Output = sol.distinctNames(ideas) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n * 26^n)\n" )
