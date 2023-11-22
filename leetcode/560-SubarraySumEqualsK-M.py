class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        sum = 0
        dic = {}
        dic[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in dic:
                count += dic[sum-k]
            dic[sum] = dic.get(sum, 0)+1
        return count

sol = Solution()
nums = [1,1,1]
k = 2
ExpectedOutput = 2
Output = sol.subarraySum(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(n)\n" )




        