# LeetCode
# 1. Two Sum (Easy)
# Author : Darshan Radadiya.
class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return(hashMap[diff], i)
            hashMap[n] = i
        return 
sol = Solution()
print(sol.twoSum([1,2,3,4,5],7))