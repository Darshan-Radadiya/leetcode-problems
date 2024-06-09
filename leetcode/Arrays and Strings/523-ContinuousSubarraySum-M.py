class Solution:
    def checkSubArraySum(self, nums: list[int], k: int) -> bool:
        hashmap = {0:-1}
        prefixSum=0
        
        for i,j in enumerate(nums):
            prefixSum+=j
            if prefixSum%k in hashmap:
                if i-hashmap[prefixSum%k]>=2:
                    return True
                else:
                    continue
            hashmap[prefixSum%k]=i
        return False
         
sol = Solution()
nums = [23,2,4,6,6]
k = 6
ExpectedOutput = True
Output = sol.checkSubArraySum(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )
