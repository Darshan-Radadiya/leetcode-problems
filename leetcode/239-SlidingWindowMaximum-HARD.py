from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        ## BRUTE FORCE

        # res = []
        # for i in range(len(nums) - k + 1):
        #     currMax = 0
        #     for j in range(i, i+k):
        #         print(j)
        #         currMax = max(currMax, nums[j])
        #     res.append(currMax)
        # return (res)

        ## OPTIMIZED WITH DEQUEUE

        l = 0
        res = []
        dq = deque([])

        for r in range(len(nums)):
            while dq and nums[r] >= nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            if dq[0] < l:
                dq.popleft()

            if r >= k - 1:
                res.append(nums[dq[0]])
                l += 1

        return res
            
sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
# nums = [7,2,4]
# k = 2
ExpectedOutput = [3,3,5,5,6,7]
Output = sol.maxSlidingWindow(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
