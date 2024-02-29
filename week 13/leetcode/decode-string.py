class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substring = ''
                while stack and stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()  # Remove '['
                
                count = ''
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                
                substring = substring * int(count)
                stack.append(substring)
        
        return ''.join(stack)
