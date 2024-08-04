from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
         # arr = [1,0,2,3,0,4,5,0]
        zeroes = 0

        for ele in arr:
            if ele == 0:
                zeroes += 1
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0

        #  Without extra space 

        #  With extra space 
        # i = 0
        # j = 0
        # res = [0]*(len(arr)+1)
        # while i < len(arr)-1:
        #     if arr[i] == 0 and j+1 < len(arr)-1:
        #         res[j] = 0
        #         res[j+1] = 0
        #         j += 2
        #     else:
        #         res[j] = arr[i]
        #         j += 1
        #     i += 1 
        # arr = res
        # print(res)
        

sol = Solution()
arr = [1,0,2,3,0,4,5,0]
ExpectedOutput = [1,0,0,2,3,0,0,4]
Output = sol.duplicateZeros(arr) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space is O(1)\n" )