class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:

        first_min = second_min = float("inf")

        for p in prices:
            if p < first_min:
                second_min, first_min = first_min, p
            else:
                second_min = min(second_min,p)

        leftover = money - (first_min + second_min)

        return leftover if leftover >= 0 else money


sol = Solution()
prices = [1,2,2]
money = 3
ExpectedOutput = 0
Output = sol.buyChoco(prices,money) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
