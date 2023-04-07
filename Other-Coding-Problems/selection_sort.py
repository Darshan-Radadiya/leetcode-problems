# Time complexity = O(n^2) - in all 3 case.

def selectionsort(arr):
    n = len(arr)

    for i in range(0, n-1):
        minimum = i

        for j in range(i, n):
            if arr[j] < arr[minimum]:
                minimum = j

        temp = arr[minimum]
        arr[minimum] = arr[i]
        arr[i] = temp
    
    return arr
        
inp = [52,63,85,42,12,9,5,45]
print(selectionsort(inp))    