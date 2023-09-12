class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2
            curr_sqrt = mid ** 2
            if curr_sqrt == num:
                return True
            elif curr_sqrt > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


sol = Solution()
n = 16
ExpectedOutput = True
Output = sol.isPerfectSquare(n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log(n) \n" )

        