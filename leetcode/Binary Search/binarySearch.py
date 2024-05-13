
# recursive 
def binarySearchRecursive(arr, n):

    if not arr:  # Base case: If the array is empty, the element is not found.
        return False
    mid = len(arr) // 2 
    if n == arr[mid]:
        return True
    elif n < arr[mid]:
        return binarySearchRecursive(arr[:mid], n)
    else:
        return binarySearchRecursive(arr[mid+1:], n)
    

# Iterative
def binarySearchIterative(arr,n):

    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if n == arr[mid]:
            return True
        elif arr[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(binarySearchRecursive([1,2,5,7,8,10,15,16,20,24,25,26],250)) # False
print(binarySearchIterative([1,2,5,7,8,10,15,16,20,24,25,26],25))  # True

print(".....Time Complexities.......")

print("Best case complexity: O(1)")
print("Average case complexity: O(log n)")
print("Worst case complexity: O(log n)")

print("......Space Complexity........")
print("The space complexity of the binary search is O(1)")



    
