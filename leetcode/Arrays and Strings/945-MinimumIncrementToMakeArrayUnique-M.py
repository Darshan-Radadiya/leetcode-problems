from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # O( n log n)
        nums = sorted(nums)
        res, incrementsReq = 0, 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                incrementsReq = nums[i -1] + 1 - nums[i]
                res += incrementsReq
                nums[i] = nums[i - 1] + 1
        return res

        # O(n + max(nums)) TSC
        n = len(nums)
        max_val = max(nums)
        min_increments = 0

        # Create a frequencyCount array to store t5he frequency of each value in nums
        frequency_count = [0] * (n + max_val + 1)

        # Populate frequencyCount array with the frequency of each value in nums
        for val in nums:
            frequency_count[val] += 1

        # Iterate over the frequencyCount array to make all values unique
        for i in range(len(frequency_count)):
            if frequency_count[i] <= 1:
                continue

            # Determine excess occurrences, carry them over to the next value,
            # ensure single occurrence for current value, and update min_increments.
            duplicates = frequency_count[i] - 1
            frequency_count[i + 1] += duplicates
            frequency_count[i] = 1
            min_increments += duplicates

        return min_increments

sol = Solution()
nums = [3,2,1,2,1,7]
ExpectedOutput = 6
Output = sol.minIncrementForUnique(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n) and O(n + max(nums))\n" )
