from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def lowerBoundBS(arr, target):
            l, r = 0, len(arr)
            while l < r:
                mid = l + (r - l) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        # Patience sort O(n log n)
        sortedArr = []
        for n in nums:
            i = lowerBoundBS(sortedArr, n)
            if i == len(sortedArr):
                sortedArr.append(n)
            else:
                sortedArr[i] = n
        return len(sortedArr)

        # O(n^2) Top Down
        n = len(nums)
        # Initialize memoization array with -1
        memo = [[-1] * (n + 1) for _ in range(n)]
        
        def solve(i, prevIndex):
            if i == n:
                return 0
            if memo[i][prevIndex + 1] != -1:
                return memo[i][prevIndex + 1]
            take = 0
            if prevIndex == -1 or nums[prevIndex] < nums[i]:
                take = 1 + solve(i + 1, i)
            skip = solve(i + 1, prevIndex)
            memo[i][prevIndex + 1] = max(take, skip)
            return memo[i][prevIndex + 1]
        
        return solve(0, -1)

        # brute force O(n^2) Bottom up
        dp = [1] *(len(nums))
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],(dp[j] + 1))
        return max(dp)  



sol = Solution()
nums = [10,9,2,5,3,7,101,18]
ExpectedOutput = 4
Output = sol.lengthOfLIS(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^2)\n" )
