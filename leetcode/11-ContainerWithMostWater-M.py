class Solution:
    def maxArea(self, height) -> int:
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res,area)

            if height[left] < height[right]:
                left += 1
            elif height[right] <= height[left]:
                right -= 1
                
        return res 

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
Output = 49
print("Output is", sol.maxArea(height))
print("Expected Output:",Output)