class Solution:
    def climbStairs(self, n):
        one = 1 
        two = 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one

sol = Solution()
print(sol.climbStairs(5))   