class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

        # Time and Space O(n)
        # prefixSum = [0]*len(arr)
        # prefixSum[0] = arr[0]
        # for i in range(1,len(arr)):
        #     prefixSum[i] += prefixSum[i-1] + arr[i]
        # res = 0

        # for i in range(len(prefixSum)):
        #     if i >= k:
        #         currAvg = prefixSum[i] - prefixSum[i-k]
        #         if currAvg // k >= threshold:
        #             res += 1
        #     elif i == k-1:
        #         currAvg = prefixSum[i]
        #         if currAvg // k >= threshold:
        #             res += 1
        # return res

    # only Time O(n):
        window_sum = sum(arr[:k])
        res = 1 if window_sum // k >= threshold else 0

        # Iterate over the array, updating the window sum
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum // k >= threshold:
                res += 1

        return res

sol = Solution()
arr = [2,2,2,2,5,5,5,8]
k = 3
t = 4
ExpectedOutput = 7
Output = sol.numOfSubarrays(arr, k, t) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n) and Space Complexity is O(1)\n" )
