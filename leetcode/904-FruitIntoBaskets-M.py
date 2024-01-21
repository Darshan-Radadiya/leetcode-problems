from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l, r = 0, 0
        res, total = 0, 0
        basket = defaultdict(int)
        while r < len(fruits):
            basket[fruits[r]] += 1
            total += 1
            while l < len(fruits) and len(basket) > 2:
                basket[fruits[l]] -= 1
                total -= 1
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l += 1
            res = max(res, total)
            r += 1
            
        return res
    
fruits = [1,2,3,2,2]
ExpectedOutput = 4
sol = Solution()
Output = sol.totalFruit(fruits) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(2n) == O(n)\n" )

