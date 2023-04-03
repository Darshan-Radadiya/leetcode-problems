class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        uniqueSet = set()
        for number in nums:
            if number not in uniqueSet:
                uniqueSet.add(number)
            else:
                return True
        return False
        
sol = Solution()
print(sol.containsDuplicate([1,2,3,2,5,6,5,4]))

