class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        
        def binarySearch(s):
            l, r = 0, len(potions) - 1
            while l <= r:
                mid = l + ((r - l) // 2)
                if potions[mid] * s >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            return (len(potions) - l)

        res = []
        potions.sort()
        for s in spells:
            pairs = binarySearch(s)
            res.append(pairs)
        return res

sol = Solution()
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
ExpectedOutput = [4,0,3]
Output = sol.successfulPairs(spells, potions, success) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and space Complexity is: O(log(n) + m log(n)) \n" )