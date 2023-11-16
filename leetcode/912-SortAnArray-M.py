class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
    
        if len(nums) > 1: 
            mid = (len(nums)) // 2
            left = nums[:mid]
            right = nums[mid:]

            self.sortArray(left)
            self.sortArray(right)

            i = j = k = 0
            while (i < len(left) and j < len(right)):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while (i < len(left)):
                nums[k] = left[i]
                i += 1
                k += 1

            while (j < len(right)):
                nums[k] = right[j]
                j += 1
                k += 1
        return nums
    
sol = Solution()
nums = [5,1,1,2,0,0]
ExpectedOutput = [0,0,1,1,2,5]
Output = sol.sortArray(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n)\n" )
