from collections import deque
from typing import List
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        res = 0

        for i in range(len(nums)):
            
            while q and i > q[0] + k - 1:
                q.popleft()
            
            if (nums[i] + len(q)) % 2 == 0:
                if i + k > len(nums):
                    return -1
                else:
                    res += 1
                    q.append(i)
        return res

sol = Solution()
nums = [0,0,0,1,0,1,1,0]
k = 3
ExpectedOutput = 3
Output = sol.minKBitFlips(nums, k) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(n)\n" )
