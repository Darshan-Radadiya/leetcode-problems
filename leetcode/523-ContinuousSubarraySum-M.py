class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        hashmap = {}
        hashmap[0]=-1
        summ=0
        for i,j in enumerate(nums):
            summ+=j
            if summ%k in hashmap.keys():
                if i-hashmap[summ%k]>=2:
                    return True
                else:
                    continue
            hashmap[summ%k]=i
        return False
    
sol = Solution()
nums = [23,2,4,6,6]
ExpectedOutput = 7
Output = sol.singleNonDuplicate(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) \n" )
