class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        for i in range(len(numbers)):
            if left <= right:
                if numbers[left] + numbers[right] == target:
                    return [left + 1, right + 1]
                elif numbers[left] + numbers[right] > target:
                    right -= 1
                elif numbers[left] + numbers[right] < target:
                    left += 1

sol = Solution()
numbers = [2,7,11,15]
target = 9 
ExpectedOutput = [1,2]
Output = sol.twoSum(numbers,target) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time & Space Complexity is: O(n) & O(1) respectively.\n" )