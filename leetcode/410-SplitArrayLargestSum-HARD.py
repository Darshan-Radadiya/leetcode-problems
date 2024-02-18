class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        def checkSubArrayPossibleMid(mid: int):
            count = 1
            currSum = 0
            for n in nums:
                if currSum + n <= mid:
                    currSum += n
                else:
                    currSum = n
                    count += 1
            return count <= k

        l, r = max(nums), sum(nums)
        ans = r
        while l <= r:
            mid = l + (( r - l ) // 2)
            if checkSubArrayPossibleMid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1 
        return ans
sol = Solution()
nums = [7,2,5,10,8]
k = 2
ExpectedOutput = 18
Output = sol.splitArray(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n log sum(nums)) \n" )
print("Detailed Explanation... https://leetcode.com/problems/split-array-largest-sum/solutions/4744279/optimized-solution-runtime-top-89-memory-efficiency-top-99-detailed-breakdown-inside/")