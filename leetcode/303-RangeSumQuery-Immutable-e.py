class NumArray:

    def __init__(self, nums: list[int]):
        self.prefixSum = [0]*len(nums)
        self.prefixSum[0] = nums[0]
        for i in range(1,len(nums)):
            self.prefixSum[i] = nums[i]+self.prefixSum[i-1]
        return None

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left-1]


nums = [-2,0,3,-5,2,-1] 

left1, right1 = 2, 5
left, right = 0, 5

obj = NumArray(nums)
param_1 = obj.sumRange(left,right)
param_2 = obj.sumRange(left1,right1)
print(param_1)
print(param_2)
print("Time Complexity is: O(n)\n" )