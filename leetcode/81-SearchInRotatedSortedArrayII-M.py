class Solution:
    def search(self, nums: list[int], target: int) -> bool:
                
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
        
            elif nums[mid] > nums[l]:   # Left side
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
         
            elif nums[mid] < nums[l] :  # Right side
                if nums[mid] > target or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
            else:
                l += 1
        return False

sol = Solution()
nums = [1,1,13,1,1,1,1]
target = 13
ExpectedOutput = True
Output = sol.search(nums, target) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(log n) best/Avg case AND Space Complexity is: O(1)\n" )
