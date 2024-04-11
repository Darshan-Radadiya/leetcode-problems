from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combinations = []
        def dfs(i):
            # base case

            if k == len(combinations):
                res.append(combinations.copy())
                return
            if i == n+1:
                return 
            
            # consider current number or i
            combinations.append(i)
            dfs(i+1)

            # do not consider current number or i
            combinations.pop()
            dfs(i+1)

        dfs(1)
        return res

n = 4
k = 2 
sol = Solution()
ExpectedOutput = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Output = sol.combine(n,k)
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(k * 2^n)\n" )
