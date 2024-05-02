
# class Solution:
#     def twoSum(self, nums, target):
#         hashMap = {}
#         for i,n in enumerate(nums):
#             diff = target - n
#             if diff in hashMap:
#                 return(hashMap[diff], i)
#             hashMap[n] = i
#         return 
        

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        ans = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ans:
                return [ans[diff],i]
            else:
                ans[nums[i]] = i
            
sol = Solution()
print(sol.twoSum([1,2,3,4,5],7))