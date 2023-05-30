# in this problem we have m*n grid 
# in which traveler can only go down or right 
# our task is to find number of ways we can reach the top left to bottom right

def traveler(row,col,memo):
    
    key = str(row) + "," + str(col)
    if key in memo:
        return memo[key]
    if row == 0 or col == 0:
        return 0
    if row == 1 or col == 1:
        return 1
    memo[key] = traveler(row-1,col,memo) + traveler(row,col-1,memo)
    return memo[key]    
print(traveler(18,18,{}))