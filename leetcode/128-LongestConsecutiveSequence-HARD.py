# Time - O(N)
# Space = O(N) - bcs of set.

class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) >= 1:
            newSet = set(nums)
            longestSeq = 0
            for i in newSet:
                if i-1 not in newSet:
                    currentLongestSeq = 0
                    while i+currentLongestSeq in newSet:
                        currentLongestSeq += 1
                    longestSeq = max(longestSeq,currentLongestSeq)
            return longestSeq
        return 0
        

sol = Solution()
nums = [100,4,200,1,3,2]
op = sol.longestConsecutive(nums)
print("Expected Output: 4")
print("Output: \t",op )
