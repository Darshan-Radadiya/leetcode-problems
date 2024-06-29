class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i, val in enumerate(nums):

            if i > 0 and val == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = val + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([val,nums[left],nums[right]])
                    left += 1
                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1
        return res
    
sol = Solution()

# nums = [-1,0,1,2,-1,-4]
nums = [-1,0,1,0]
Output = [[-1,-1,2],[-1,0,1]]

print("Expected Output: ", Output)
print("Output: ", sol.threeSum(nums))
