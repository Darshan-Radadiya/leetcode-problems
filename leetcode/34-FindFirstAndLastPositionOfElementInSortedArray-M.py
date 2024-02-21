class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Time complexity is O(lon n) + O(n) = O(n) in worst case. O(n) is bcs of the while loop
        # Imagine the nums with value 1 and len 10^5 and target is also 1.
        # l, r = 0, len(nums)-1
        # res = []
        # startIndx, endIndx = -1 , -1
        # if r == 0 and target in nums:
        #     return [0,0]
        # elif r == 0 and target not in nums:
        #     return [-1,-1]
        # while l <= r:
        #     mid = l + ((r - l) //2)
        #     if nums[mid] == target:
        #         startIndx, endIndx = mid, mid
        #         while mid != 0 and nums[mid] == nums[mid - 1]:
        #             mid = mid - 1
        #             startIndx = mid
        #         while mid != len(nums) - 1 and nums[mid] == nums[mid+1]:
        #             mid = mid + 1
        #             endIndx = mid
        #         return [startIndx,endIndx]
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return [startIndx,endIndx]
    
    # Optimized solution which will be O(log n) + O(log n) in all the cases.
    
        def binarySearch(nums, target, rightBiased):
            l, r = 0, len(nums)-1
            idx = -1
            while l <= r:
                mid = l + ((r - l) // 2)
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    idx = mid
                    if rightBiased:
                        l = mid + 1
                    else:
                        r = mid - 1
            return idx

        startIdx = binarySearch(nums, target, False)
        endIdx = binarySearch(nums, target, True)
        return [startIdx, endIdx]

