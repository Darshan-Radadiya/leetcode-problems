class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        # this type of array is called bitonic array
        # arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
        # 1 3 4 6 9  14  11 7 2
        #  Binary search
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + ((r - l) // 2)
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid 
            if arr[mid+1] > arr[mid-1]:
                l = mid + 1
            else:
                r = mid - 1

sol = Solution()
arr = [1,2,3,4,5,14,10,9,8,7,3]
ExpectedOutput = 5
Output = sol.peakIndexInMountainArray(arr) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log n) \n" )
