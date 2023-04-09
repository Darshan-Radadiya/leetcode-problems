class Solution:
    def topKFrequent(self, nums, k):
        
        if len(nums) <= 1:
            return nums
        frequencyOfNum = {}
        count = [[] for i in range(len(nums)+1)]
        for n in nums:
            frequencyOfNum[n] = 1 + frequencyOfNum.get(n,0)
        for key,val in frequencyOfNum.items():
            count[val].append(key)
            print(key,val)

        print(frequencyOfNum)
        print(count)
        res = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res

# o(N)
sol = Solution()
nums = [1,1,1,2,80,80,80,80,80,2,3,4,4,4]
k = 2
print("Expected Output: [1,2]")
print("Output: ", sol.topKFrequent(nums,k))