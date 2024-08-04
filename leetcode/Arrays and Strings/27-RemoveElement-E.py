class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        # when you slice a list it creates a new list object that references the original list's elements
        nums[:] = [n for n in nums if n != val]
        return len(nums)

        #or

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k 


