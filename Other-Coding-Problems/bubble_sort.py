#Time complexity = O(N^2) - for worst and average case
# for best case its O(N)
# it is opposite of a selection sort like here we are replacing the max with adjacent value.

def bubbleSort(arr):

    n = len(arr)
    swapHappened = 0

    for i in range(n, 1, -1):
        for j in range(0,i-1):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapHappened = 1
        
        # this is for the best case. If arr is already sorted then after one iteration over arr not a single swap wil happen
        # so we can say its already sorted. 
        if swapHappened == 0:
            return arr
        
    return arr

INPUT = [2,56,1,89,2,640,65,626,3]
print(bubbleSort(INPUT))
