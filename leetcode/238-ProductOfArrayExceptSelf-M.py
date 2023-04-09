# time = O(N)
# space = O(1)

class Solution:
    def productExceptSelf(self, nums):
        
        res = [[1] for i in range(len(nums))]

        multiForPrefix = 1
        for i in range(len(nums)):
           res[i] = multiForPrefix
           multiForPrefix *= nums[i]

        multiForPostfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= multiForPostfix
            multiForPostfix *= nums[i]
        print(res)

sol = Solution()
nums = [-1,1,0,-3,3]
print("Expected Output: [24,12,8,6]")
print("Output: ", sol.productExceptSelf(nums))