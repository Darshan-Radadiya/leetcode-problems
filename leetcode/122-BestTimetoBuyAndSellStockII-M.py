class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
    

sol = Solution()
prices = [7,1,5,3,6,4]
ExpectedOutput = 7
Output = sol.maxProfit(prices) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(n)\n" )

