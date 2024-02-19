class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                    continue
            elif s[i] == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                    continue
            elif s[i] == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                    continue
            stack.append(s[i])
        
        if len(stack) > 0: return False
        return True