class Solution:
    def isValid(self, s: str) -> bool:

        Map = { "}":"{", "]":"[", ")":"(" }
        stack = []

        for b in s:
            if b in Map:
                if stack and stack[-1] == Map[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return True if not stack else False


sol = Solution()
s = "()[]{}"
Output = True
print("Expected Output:", Output)
print("Output: ", sol.isValid(s))