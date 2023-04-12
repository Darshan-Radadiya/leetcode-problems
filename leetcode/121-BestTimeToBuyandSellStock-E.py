class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxProfit = max(maxProfit,profit)
            else:
                l = r
            r += 1

        return maxProfit

sol = Solution()
prices = [2,1,4]
# prices = [7,1,5,3,6,4]
print("Expected Output: 5")
print("Output: ", sol.maxProfit(prices))