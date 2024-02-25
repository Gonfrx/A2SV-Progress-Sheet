class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                        continue
            stack.append(s[i])

        return len(stack)

