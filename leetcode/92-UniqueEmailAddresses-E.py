class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        uniqueMails = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".","")
            uniqueMails.add(local+"@"+domain)
        print(uniqueMails)
        return len(uniqueMails)


sol = Solution()
emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
ExpectedOutput = 2
Output = sol.numUniqueEmails(emails) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n*m). Here n is length of emails list and m is the length of the each email.\n" )
