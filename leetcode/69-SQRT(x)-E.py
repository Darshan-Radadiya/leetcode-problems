class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        res = x
        while left <= right:
            mid = (left + right) // 2
            num = mid * mid
            if num == x:
                return mid
            elif num > x:
                res = min(res, mid - 1)
                right = mid - 1
            else:
                left = mid + 1
        return res



sol = Solution()
x = 8
ExpectedOutput = 2
Output = sol.mySqrt(x) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log(n) \n" )

        