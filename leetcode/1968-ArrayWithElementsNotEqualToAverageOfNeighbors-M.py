class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # Wiggle Sort solution
        #
        # for i in range(1,len(nums)):
        #     if (i % 2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i-1]):
        #         nums[i], nums[i-1] = nums[i-1], nums[i]
        # return nums

        nums.sort()
        l, r= 0, len(nums) - 1
        res = []
        while len(res) != len(nums):
            res.append(nums[l])
            l += 1

            if l <= r:
                res.append(nums[r])
                r -= 1

        return res

sol = Solution()
input = [1,2,3,4,5]
ExpectedOutput =  [1,5,2,4,3]
Output = sol.rearrangeArray(input) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(1)\n" )