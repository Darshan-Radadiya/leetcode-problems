class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n = len(people) - 1
        l, r = 0, n 
        res = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            res += 1
    
        return res

sol = Solution()
people = [3,5,3,4]
limit = 5
ExpectedOutput = 4
Output = sol.numRescueBoats(people, limit) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(n) \n" )
