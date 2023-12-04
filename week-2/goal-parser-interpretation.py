class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] == 'G': 
               temp = ans + 'G'
               ans = temp
            elif command[i] == '(': 
                if command[i+1] == ')': 
                     temp = ans + 'o'
                     ans = temp
                     i += 1
                else:
                    temp = ans + "al"
                    ans = temp
                    i += 3
        return ans 
                     