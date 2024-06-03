class Solution:
    def largestDivisibleSubset(self, nums):
        # TC - O(n^2) and SC - O(n) Bottom up
        # by sorting we can make sure that we don't need to check i%j and j%i.
        #  we can only check j%i and that will be sufficient. j is largest and i is smaller than j.
        #  
        nums.sort()
        n = len(nums)
        memo = {}
        res = []
        def solve(i):
            if i == n: return []
            if i in memo: return memo[i]

            res = [nums[i]]
            for j in range(i+1, n):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + solve(j)
                    if len(temp) > len(res):
                        res = temp
            memo[i] = res            
            return res
        
        for i in range(n):
            temp = solve(i)
            if len(temp) > len(res):
                res = temp
        return res


        # TC and SC - O(n^2) Top down approach.
        def generate(idx, nums, prev, memo):
            if idx >= len(nums):
                return []

            if (idx, prev) in memo:
                return memo[(idx, prev)]

            taken = []
            if prev == -1 or nums[idx] % prev == 0:
                taken = [nums[idx]] + generate(idx + 1, nums, nums[idx], memo)
                
            not_taken = generate(idx + 1, nums, prev, memo)

            result = max(taken, not_taken, key=len)
            memo[(idx, prev)] = result
            return result

        nums.sort()
        memo = {}
        return generate(0, nums, -1, memo)

sol = Solution()
nums = [5,9,18,54,108,540,90,180,360,720]
ExpectedOutput = [9,18,90,180,360,720]
Output = sol.largestDivisibleSubset(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n^2)\n" )
