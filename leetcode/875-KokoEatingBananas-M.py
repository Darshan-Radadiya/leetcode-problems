import math
class Solution:

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        def countBanana(mid):
            numOfBananaPerHour = 0
            for p in piles:
                numOfBananaPerHour += math.ceil(p/mid)
            return numOfBananaPerHour
        
        left, right = 1, max(piles)
        res = max(piles)
        while left <= right:
            mid = (left + right) // 2

            totalTime = countBanana(mid)

            if totalTime <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

sol = Solution()
piles = [30,11,23,4,20]
h = 5
ExpectedOutput = 30
Output = sol.minEatingSpeed(piles, h) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log(max(n))n)\n" )

