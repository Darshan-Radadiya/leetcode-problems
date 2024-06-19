from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # as we can see in the bloomDay arr. 
        # we required minimum number/day to bloom one flower and
        # we can say for sure if we take maximum number/day then we can form make the bouquets.
        # so we found the range min to max. now our job is to find the minimum number from this range.
        # so instead of doing O(n) search for all the ele in range we can do the Binary serach.
        # O(N log D)
        def isPossible(day):
            count = 0
            numOfBouquets = 0
            for d in bloomDay:
                if d <= day:
                    count += 1
                    if count == k:
                        numOfBouquets += 1
                        count = 0
                else:
                    count = 0
            return numOfBouquets >= m

        if m * k > len(bloomDay):
            return -1

        l = min(bloomDay)  # minDaysToStartBlooming
        r = max(bloomDay)  # maxDaysToEndBlooming
        res = -1
        while l <= r:
            mid = l + ((r - l) // 2)

            if isPossible(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res

sol = Solution()
bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
ExpectedOutput = 12
Output = sol.minDays(bloomDay, m, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(N log D) and O(1)\n" )

