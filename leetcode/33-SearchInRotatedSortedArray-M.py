class Solution:
    def search(self, nums,target):

        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # left portion
            elif nums[mid] >= nums[l]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right portion
            else:
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
            
        


sol = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
Output = 4

# nums = [4,5,6,7,0,1,2]
# target = 3
# Output = -1

# nums = [1]
# target = 0
# Output = -1

print("Expected Output:", Output)
print("Output: ", sol.search(nums,target))