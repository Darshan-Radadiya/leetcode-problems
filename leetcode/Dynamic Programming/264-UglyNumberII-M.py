class Solution:
    def nthUglyNumber(self, n: int) -> int:
        resArr = [0 for i in range(n+1)]
        i2 = 1
        i3 = 1
        i5 = 1
        resArr[1] = 1
        for i in range(2, n+1):
            i2UglyNumber = resArr[i2]*2
            i3UglyNumber = resArr[i3]*3
            i5UglyNumber = resArr[i5]*5
            minUglyNumber = min(i2UglyNumber, i3UglyNumber, i5UglyNumber)
            resArr[i] = minUglyNumber
            if minUglyNumber == i2UglyNumber:
                i2 += 1
            if minUglyNumber == i3UglyNumber:
                i3 += 1
            if minUglyNumber == i5UglyNumber:
                i5 += 1
        return resArr[n]

sol = Solution()
n = 16
ExpectedOutput = 25
Output = sol.nthUglyNumber(n) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
