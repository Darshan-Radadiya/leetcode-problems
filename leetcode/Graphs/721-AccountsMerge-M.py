from typing import List
from collections import defaultdict 
class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)] 
        self.rank = [1] * n

    def find(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        uParent = self.find(u)
        vParent = self.find(v)
        if uParent == vParent:
            return 
        if self.rank[uParent] > self.rank[vParent]:
            self.parent[vParent] = u
        elif self.rank[vParent] > self.rank[uParent]:
            self.parent[uParent] = v
        else:
            self.parent[uParent] = v
            self.rank[uParent] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind(len(accounts))
        emailToAccDict = {} # email - idx
        #  based on the index we will union the two different accounts.
        #  idx here serves as a parent/node.
        for i in range(len(accounts)):
            for e in accounts[i][1:]:
                if e in emailToAccDict:
                    dsu.union(i, emailToAccDict[e])
                else:
                    emailToAccDict[e] = i

        # group the emails that belongs to the same parent.
        # most difficult part of the problem i think.
        emailGroup = defaultdict(list)
        for e, i in emailToAccDict.items():
            parent = dsu.find(i)
            emailGroup[parent].append(e)
        
        # at the end go over above email group to create the final res array.
        res = []
        for i, e in emailGroup.items():
            res.append([accounts[i][0]] + sorted(e))
        return res
        
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
ExpectedOutput = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
sol = Solution()
Output = sol.accountsMerge(accounts) 
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is:O(NK * logNK + NK * alpha(N)))\n" )
