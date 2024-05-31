# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True

class Solution:
    def verify_potential_candidate(self, potential_candidate, n):
        for i in range(n):
            if i == potential_candidate:
                continue
            if not knows(i, potential_candidate) or knows(potential_candidate, i):
                return False
        return True
    # main function
    def findCelebrity(self, n: int) -> int:
        potential_candidate = 0
        for i in range(n):
            if knows(potential_candidate, i):
                potential_candidate = i
        return potential_candidate if self.verify_potential_candidate(potential_candidate, n) else -1
        
print("Time and Space complexity is O(n) and O(1) respectively")