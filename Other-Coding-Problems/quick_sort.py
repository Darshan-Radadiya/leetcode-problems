# this is better than merge sort because here we are not using extra array to store sorted array.
# Time complexity for best, avg = O(n Log n) 
# Time complexity for worst = O(n^2) 
# Space Complexity = O(log n)

def quickSort(arr,low,high):
    if low < high:
        partitionIndex = partition(arr,low,high)
        quickSort(arr,low,partitionIndex - 1)
        quickSort(arr,partitionIndex+1,high)
    
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j

inp = [52,63,85,42,12,9,5,45]
quickSort(inp,0,len(inp)-1)
print("Output\t", inp)
print("Expected Output\t: [5, 9, 12, 42, 45, 52, 63, 85]")
