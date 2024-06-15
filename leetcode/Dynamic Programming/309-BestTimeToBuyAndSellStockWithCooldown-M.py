from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # Initialize the dp array
        dp = [0] * (n + 2)
        
        # Loop through each day starting from the first day
        for i in range(1, n):
            max_profit = 0
            for j in range(i):
                # Calculate the profit if we sell on day i and bought on day j
                profit = prices[i] - prices[j] + (dp[j-2] if j >= 2 else 0)
                max_profit = max(max_profit, profit)
            dp[i] = max(dp[i-1], max_profit)
        
        return dp[n-1]

        # Top Down O(n^2)
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n+1)]
        def solve(day, isBuy):
            if day >= n:
                return 0
            if memo[day][isBuy] != -1:
                return memo[day][isBuy]
            profit = 0
            if isBuy:
                buy = solve(day+1, False) - prices[day]
                notBuy = solve(day+1, True)
                profit = max(profit,buy, notBuy)
            else:
                sell = prices[day] + solve(day+2, True)
                notSell = solve(day+1,False)
                profit = max(profit,sell, notSell)
            
            memo[day][isBuy] = profit
            return  memo[day][isBuy]
        
        buy = True
        return solve(0, buy)

sol = Solution()
prices = [1,2,3,0,2]
ExpectedOutput = 3
Output = sol.maxProfit(prices) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^2) \n" )
