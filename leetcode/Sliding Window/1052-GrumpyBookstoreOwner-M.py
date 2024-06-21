from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)  # Get the number of minutes (length of customers list)
        ans = 0  # Initialize the count of satisfied customers

        # Calculate the initially satisfied customers (when the owner is not grumpy)
        for i in range(n):
            if grumpy[i] == 0:  # If the owner is not grumpy at minute i
                ans += customers[i]  # Add the number of customers to ans

        unsatis = 0  # Initialize the count of unsatisfied customers for the first window

        # Calculate the number of unsatisfied customers in the initial window of 'minutes' length
        for i in range(minutes):
            if grumpy[i] == 1:  # If the owner is grumpy at minute i
                unsatis += customers[i]  # Add the number of customers to unsatis

        max_ = unsatis  # Initialize max_ with the initial unsatisfied customer count

        # Use a sliding window to find the maximum number of unsatisfied customers in any 'minutes' window
        for i in range(minutes, n):
            # If the owner was grumpy 'minutes' minutes ago, subtract those customers as they slide out of the window
            if grumpy[i - minutes] == 1:
                unsatis -= customers[i - minutes]
            
            # If the owner is grumpy at the current minute, add those customers to unsatis
            if grumpy[i] == 1:
                unsatis += customers[i]
            
            # Update max_ to be the maximum of its current value or the updated unsatis
            max_ = max(max_, unsatis)

        # The final result is the sum of initially satisfied customers and the maximum additional customers
        # that can be satisfied by controlling the owner's grumpiness for 'minutes' period
        return ans + max_
    
sol = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
ExpectedOutput = 16
Output = sol.maxSatisfied(customers, grumpy, minutes) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
