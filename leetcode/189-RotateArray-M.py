class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        l1, r1 = 0, k - 1 
        # nums.reverse()

        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
            
        while l1 <= r1:
            nums[l1], nums[r1] = nums[r1], nums[l1]  
            l1 += 1
            r1 -= 1
        
        l2, r2 = k, len(nums)-1
        while l2 < len(nums) and l2 < r2:
            nums[l2], nums[r2] = nums[r2], nums[l2]
            l2 += 1
            r2 -= 1

        return nums


sol = Solution()
nums = [1,2,3,4,5,6,7,8,9,10]
k = 4
ExpectedOutput = [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
Output = sol.rotate(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )

