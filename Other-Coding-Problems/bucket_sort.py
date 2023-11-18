class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class Solution:
    def bucketSort(self, arr) -> int:
        n = len(arr) - 1

        max_value = max(arr)
        min_value = min(arr)

        # Determine the number of buckets based on the range of values - occupies extra space.
        # num_buckets = max_value - min_value + 1
        # print("Number of bucket is", num_buckets)
      

        tempArr = [ [] for i in range(n + 1)] 
        for i, ele in enumerate(arr):
            
            # bucket_index = ele - min_value
            bucket_index = (ele//(max_value//n))
            print(bucket_index)
            curr = tempArr[bucket_index]
            if curr:
                if curr.key > ele:
                    subCurr = curr
                    tempArr[bucket_index] = Node(ele)
                    tempArr[bucket_index].next = subCurr
                else:
                    curr.next = Node(ele)
            else:
                tempArr[bucket_index] = Node(ele)
        
        print(tempArr)

        j = 0
        for i in tempArr:
            while i:
                arr[j] = i.key
                i = i.next
                j += 1
        return arr





sol = Solution()
arr = [29, 23, 34, 45, 12, 9, 56, 43]
ExpectedOutput = [9, 12, 23, 29, 34, 43, 45, 56]
Output = sol.bucketSort(arr) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity: O(n + k), where n is the number of elements and k is the number of buckets")
print("Space Complexity: O(n), where n is the number of elements")

