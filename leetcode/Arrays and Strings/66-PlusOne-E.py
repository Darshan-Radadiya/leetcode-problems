from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         digits = [1,2,3,9,3]
#         ans =    [1,2,3,9,4]
        
        if len(digits) == 1 and digits[0]== 9:
            return [1,0]
        else:
            if digits[len(digits)-1] == 9:
                i = 1
                while (len(digits)-i) >= 0 and digits[len(digits)-i] == 9:
                    digits[len(digits)-i] = 0
                    i += 1
                if len(digits) - i >= 0:
                    digits[len(digits)-i] += 1
                else:
                    return [1] + digits
            else:
                digits[len(digits)-1] += 1
        return digits
                
        # OR

#         digits = [1,2,9]
#         ans    = [1,3,0]
        
#         digits = [1,2,3,9,9]
#         ans = [1,2,3,4,0,0]
        
#         digits = [9,9,9,9,9,9]
#         ans = [1,0,0,0,0,0,0]

#         digits = [ 9, 9 , 9]
#         ans = [ 1, 0, 1, 0]

        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If we reach this point, it means all digits were 9
        return [1] + digits

sol = Solution()
nums = [1,9,9,9]
ExpectedOutput = [2,0,0,0]
Output = sol.plusOne(nums) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )


        