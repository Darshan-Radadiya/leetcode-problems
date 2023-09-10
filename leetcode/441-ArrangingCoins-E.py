class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            total_num_of_row = (left + right) // 2
            value_fill_all_rows = (total_num_of_row / 2) * (total_num_of_row + 1)
            
            if n == value_fill_all_rows:
                return total_num_of_row
            elif n < value_fill_all_rows:
                right = total_num_of_row - 1
            else:
                left = total_num_of_row + 1
        return right





sol = Solution()
n = 8
ExpectedOutput = 3
Output = sol.arrangeCoins(n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log(n) \n" )

        