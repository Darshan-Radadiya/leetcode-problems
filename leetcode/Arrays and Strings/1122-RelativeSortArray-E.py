from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
        # Output: [22,28,8,6,17,44]

        # 28 - 1  28 - 1 22 - 1
        # 6 - 1   6  - 1 28 - 1
        # 22 - 1  22 - 1 8  - 1
        # 8 - 1   8  - 1 6  - 1
        # 44 - 1 
        # 17 - 1

        # count the freq of both array then go through the freq of second array and 
        # fill the ele of the first array in res array in sorted fashion
        # return res O(n) + O(n) + O(n) = 3 O(n log n) == O(n) and space same 3O(n) == O(n)
        
        # Step 1: Count the frequency of elements in arr1
        freqA = {}
        for ele in arr1:
            freqA[ele] = 1 + freqA.get(ele, 0)
        
        # Step 2: Initialize the result list
        res = []
        
        # Step 3: Add elements from arr2 in the correct order
        for ele in arr2:
            if ele in freqA:
                res.extend([ele] * freqA[ele])
                del freqA[ele]
        
        # Step 4: Add remaining elements from arr1 (those not in arr2) in sorted order
        remaining = sorted(freqA.keys())
        for ele in remaining:
            res.extend([ele] * freqA[ele])
        
        return res

sol = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
ExpectedOutput = [2,2,2,1,4,3,3,9,6,7,19]
Output = sol.relativeSortArray(arr1, arr2) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(k) + O(n) + O(m log m) = O(n log n) k is total ele in array1\n" )