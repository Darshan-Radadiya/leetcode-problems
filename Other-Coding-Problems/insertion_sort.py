#Time complexity = O(N^2) - for worst and average case
# for best case its O(N)


def insertionSort(arr):
    n = len(arr)
    swapHappened = 0
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1

            # below three line is for best case. 
            swapHappened = 1
        if swapHappened == 0:
            return arr
    
    return arr
        
inp = [52,63,85,42,12,9,5,45]
print(insertionSort(inp))    