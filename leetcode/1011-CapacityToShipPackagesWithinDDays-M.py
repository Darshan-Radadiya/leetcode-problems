class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            capacity = (l + r) // 2
            currSum = 0
            ships = 1
            for w in weights:
                if currSum + w <= capacity:
                    currSum += w
                else:
                    ships += 1 
                    currSum = w
            if ships > days:
                l = capacity + 1
            else:
                r = capacity - 1
        return l
    

sol = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
ExpectedOutput = 15
Output = sol.search(weights, days) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n log m) n = for loop and log m = binary search \n" )
