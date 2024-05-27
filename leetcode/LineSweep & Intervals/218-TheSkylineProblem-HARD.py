from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ##########################################
        ######## BRUTE FORCE O(N^2) & O(N) #######
        ##########################################

        # Sort the unique positions of all the edges.
        # positions = set()
        for l,r,h in buildings:
            positions.add(l)
            positions.add(r)
        positions = sorted(list(positions))
        # Hast table 'edge_index_map' to record every {position : index} pairs in edges.
        edge_index_map = {}
        for i, x in enumerate(positions):
            edge_index_map[x] = i
        
        heights = [0] * len(positions)
        # Iterate over all the buildings.
        for left, right, height in buildings:
            # For each building, find the indexes of its left
            # and right edges.
            left_idx = edge_index_map[left]
            right_idx = edge_index_map[right]

            # Update the maximum height within the range [left_idx, right_idx)
            for i in range(left_idx, right_idx):
                heights[i] = max(heights[i], height)
        
        answer = []
        # Iterate over 'heights'.
        for i in range(len(heights)):
            curr_height = heights[i]
            curr_x = positions[i]

            # Add all the positions where the height changes to 'answer'.
            if not answer or answer[-1][1] != curr_height:
                answer.append([curr_x, curr_height])
        return answer

        ##########################################
        ######## BRUTE FORCE O(N^2) & O(N) #######
        ############## Line Sweep ################
        ##########################################

        # Sort the unique positions of all the edges.
        positions = set()
        for l,r,h in buildings:
            positions.add(l)
            positions.add(r)
        positions = sorted(list(positions))

        ans = []
        for position in positions:
            maxHeight = 0
            for l, r, h in buildings:
                if l <= position < r:
                    maxHeight = max(maxHeight, h)
            
            if not ans or ans[-1][1] != maxHeight:
                ans.append([position, maxHeight])
        return ans

sol = Solution()
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
ExpectedOutput = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Output = sol.getSkyline(buildings) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n Log n)\n" )
