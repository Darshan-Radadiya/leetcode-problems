class Solution:
    def trap(self, height: list[int]) -> int:

        left, right = 0, len(height) - 1
        res = 0
        leftMax, rightMax = height[left], height[right]

        while left < right:

            if leftMax < rightMax :
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        return res

sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
ExpectedOutput = 6
Output = sol.trap(height) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
print("Space Complexity is: O(1)\n" )
