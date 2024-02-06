class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stck = []
        for a in asteroids:
            while stck and a < 0 and stck[-1] > 0:
                diff = a + stck[-1]
                if diff < 0:
                    stck.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stck.pop() 
            if a:
                stck.append(a)
        return stck

asteroids = [-1,3,2,-3]
ExpectedOutput = [-1]
sol = Solution()
Output = sol.asteroidCollision(asteroids) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
