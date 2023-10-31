class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        tempStack = []
        res = [-1] * len(nums1)
        nums1Map = {}
        for i in range(len(nums1)):
            nums1Map[nums1[i]] = i

        for i in range(len(nums2)):
            currEle = nums2[i]
            while tempStack and currEle > tempStack[-1]:
                currStackVal = tempStack.pop()
                idx = nums1Map[currStackVal]
                res[idx] = currEle
            
            if currEle in nums1Map:
                tempStack.append(currEle)
        return res

        

sol = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
ExpectedOutput = [-1,3,-1]
Output = sol.nextGreaterElement(nums1,nums2) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(nums1+nums2)\n" )
             





        
