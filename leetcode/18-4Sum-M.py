class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        # res for final list or quadruplets and currQuad for current quadruplets.
        res, currQuad = [], []

        # this function can do the sum of k numbers like 5sum or 6sum
        def kSum(k, startIdx, target):
            # if k 2 we need to just use two pointer technique by sorting the arr.
            if k != 2:
                for i in range(startIdx, len(nums)-k+1):
                    if i > startIdx and nums[i] == nums[i-1]:
                        continue
                    currQuad.append(nums[i])
                    kSum(k-1, i+1,target-nums[i])
                    currQuad.pop()
                return
            
            #Two pointer two sum problem.
            l, r = startIdx, len(nums)-1
            while l < r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    res.append(currQuad + [nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        kSum(4, 0, target)
        return res


sol = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
ExpectedOutput = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Output = sol.fourSum(nums, target) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^k) where k is num of sum - 1 so here it will be n^3 \n" )
