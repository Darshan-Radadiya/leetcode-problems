from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #  brute force will be sort the arr 
        #  then go over that new sorted arr and check what are the ele not 
        #  matching with the original arr and return that count.
        #  O(n log n) + O(n) == O(n log n)
        #  it turns out that this is the only way to solve this problem.

        # will use merge sort bcs its having O(n log n) in all cases.
        # heap sort also have same complexity but merge sort is lil bit easy to implement.
        def mergeSort(arr):
            if len(arr) > 1:
                mid = (len(arr)) // 2
                leftPart = arr[:mid]
                rightPart = arr[mid:]

                mergeSort(leftPart)
                mergeSort(rightPart)

                i = j = k = 0

                while i < len(leftPart) and j < len(rightPart):
                    if leftPart[i] < rightPart[j]:
                        arr[k] = leftPart[i]
                        i += 1
                    else:
                        arr[k] = rightPart[j]
                        j += 1
                    k += 1
                
                while i < len(leftPart):
                    arr[k] = leftPart[i]
                    i += 1
                    k += 1
                
                while j < len(rightPart):
                    arr[k] = rightPart[j]
                    j += 1
                    k += 1
        
        sortedArr = list(heights)
        mergeSort(sortedArr)

        diff = 0
        for i in range(len(sortedArr)):
            if sortedArr[i] != heights[i]:
                diff += 1
        return diff

sol = Solution()
heights = [1,1,4,2,1,3]
ExpectedOutput = 3
Output = sol.heightChecker(heights) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n log n) \n" )
