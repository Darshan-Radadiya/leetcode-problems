class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob_helper(nums):
            first, second = 0, 0

            for r in nums:
                t = max(r + first, second)
                first = second
                second = t
            return second

        return max( nums[0] , rob_helper(nums[1:]), rob_helper(nums[:-1]) )
    
sol = Solution()
print(sol.rob([2,3,2]))