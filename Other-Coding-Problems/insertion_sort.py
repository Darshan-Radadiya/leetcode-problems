#Time complexity = O(N^2) - for worst and average case and for best case its O(N)
# Spcace complexity = O(1)


def insertionSort(arr):
    n = len(arr)
    for i in range(0, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1
    
    return arr
        
inp = [52,63,85,42,12,9,5,45]
print(insertionSort(inp))    