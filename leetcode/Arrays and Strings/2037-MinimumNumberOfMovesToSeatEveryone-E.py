from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 1, 3, 5 - seat
        # 2, 4, 7 - student
        # 1 + 1 + 2 = 4 moves

        # 1, 4, 5, 9 - seat
        # 1, 2, 3, 6 - student
        # 0 + 2 + 2 + 3 = 7 moves

        #  sort both the arr and then find the difference between seat and student 
        # at ith position and add it in res. O(n log n)
        seats = sorted(seats)
        students = sorted(students)
        moves = 0
        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])
        return moves

        #  using counting sort bcs of the input arr size is only 100.
        #  find the max for the total size of the counting sort.
        maxPosition = max(max(seats), max(students))

        # Stores difference between number of seats and students at each position
        differences = [0] * (maxPosition)

        #  count no of available seats.
        for pos in seats:
            differences[pos - 1] += 1

        #  remove the seat by descremting the seat count if student is present at current seat.
        for student in students:
            differences[student - 1] -= 1
        
        # Calculate the number of moves needed to seat the students
        moves = 0
        unmatched = 0
        for difference in differences:
            moves += abs(unmatched)
            unmatched += difference

        return moves
    
sol = Solution()
seats = [4,1,5,9]
students = [1,3,2,6]
ExpectedOutput = 7
Output = sol.minMovesToSeat(seats, students) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
