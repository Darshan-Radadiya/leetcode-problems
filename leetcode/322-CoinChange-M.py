# class Solution:
    # def coinChange(self, coins: list[int], amount: int) -> int:
    #     dp = [amount + 1] * (amount + 1)
    #     dp[0] = 0

    #     for a in range(1, amount + 1):
    #         for c in coins:
    #             if a - c >= 0:
    #                 dp[a] = min(dp[a], 1 + dp[a - c])
    #     return dp[amount] if dp[amount] != amount + 1 else -1

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [None]*(amount+1)
        dp[0] = []
        for i in range(amount+1):
            if dp[i] != None:
                for num in coins:
                    if i+num <= amount:
                        newArr = dp[i] + [num]
                        if dp[i+num] and len(dp[i+num]) > len(newArr) or dp[i+num] == None: 
                            dp[i+num] = newArr
        return len(dp[amount]) if dp[amount] != None else -1

sol = Solution()
coins = [1,2,5]
amount = 11
ExpectedOutput = 3
Output = sol.coinChange(coins,amount) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(Amount*len(coins))\n" )
