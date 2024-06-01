class Solution:

    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]



    # def rob(self, nums: list[int]) -> int:
    #     first, second = 0, 0

    #     for r in nums:
    #         t = max(r + first, second)
    #         first = second
    #         second = t
    #     return second


sol = Solution()
print(sol.rob([1,2,3,1]))