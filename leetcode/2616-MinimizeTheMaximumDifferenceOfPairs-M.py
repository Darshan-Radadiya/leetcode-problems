class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        def canFormPairs(guessedDiff):
            i = 0
            pairCount = 0
            while i < len(nums) - 1 and pairCount < p:
                if (nums[i+1] - nums[i]) <= guessedDiff:
                    pairCount += 1
                    i += 2
                else:
                    i += 1
            return pairCount == p

        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if canFormPairs(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


sol = Solution()
nums = [10,1,2,7,1,3]
p = 2
ExpectedOutput = 1
Output = sol.minimizeMax(nums, p) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log m) AND Space Complexity is: O(1)\n" )

