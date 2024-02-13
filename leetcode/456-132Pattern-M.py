class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = [] #it will be pair of num and currMinOnLeft
        currMinOnLeft = nums[0]
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append([n, currMinOnLeft]) 
            currMinOnLeft = min(currMinOnLeft, n)
        return False

s = [3,1,4,2]
ExpectedOutput = True
sol = Solution()
Output = sol.find132pattern(s) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(2n) == O(n)\n" )
