class Solution:
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     # Binary search to find the closest element
    #     left, right = 0, len(arr) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if arr[mid] < x:
    #             left = mid + 1
    #         else:
    #             right = mid

    #     # Initialize pointers for finding k closest elements
    #     left, right = left - 1, left

    #     # Expand the window to find k elements
    #     while right - left - 1 < k:
    #         if left == -1:  # If left pointer goes out of bound
    #             right += 1
    #         elif right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
    #             left -= 1
    #         else:
    #             right += 1

    #     return arr[left + 1:right]
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l, r = 0, len(arr) - k
        while l < r:
            mid = (l+r) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l+k]

arr = [1,2,3,4,5]
k = 4
x = 3
sol = Solution()
Output = sol.findClosestElements(arr, k, x) 
ExpectedOutput = [1, 2, 3, 4]
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity for first approach is: O(logn + k) and for second approach its O((log - k) + k)\n" )
 
