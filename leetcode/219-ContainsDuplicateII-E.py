class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
    
sol = Solution()
nums = [1,0,1,1]
k = 1
ExpectedOutput = 3
Output = sol.containsNearbyDuplicate(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(Amount*len(coins))\n" )
