from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Three pointer sliding window
        l, mid = 0,0
        res = 0
        odd = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
            
            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                mid = l
            
            if odd == k:
                while not nums[mid] % 2:
                    mid += 1
                res += (mid - l) + 1
        return res
    
sol = Solution()
nums = [1,1,2,1,1,2]
k = 3
ExpectedOutput = 3
Output = sol.numberOfSubarrays(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
