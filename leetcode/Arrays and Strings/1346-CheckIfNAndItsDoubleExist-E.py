class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        # Input: arr = [10,2,5,3]
        # Output: true
        
        # Input: arr = [3,1,7,11]
        # Output: false
        
        # i != j and arr[i] == 2 * arr[j]
        
        # 2,3,5,10
        
        seen = set()
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False

sol = Solution()
nums = [10, 2, 4, 5, 34]
ExpectedOutput = True
Output = sol.checkIfExist(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n) and Space O(n)\n" )
