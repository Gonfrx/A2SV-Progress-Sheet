class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [] 
        counter = t = 0

        for i in range(len(s)):
            if s[i] == ')':
                    if stk[-1][1] == 0:
                        counter += 1
                        stk.pop()
                        if stk: 
                            stk[-1][1]+=1
                        else:
                            t += counter
                            counter = 0
                    elif stk[-1][1] > 0: 
                        temp = stk[-1][1] *2 
                        counter = temp 
                        stk.pop()
                        if stk:
                            stk[-1][1] += temp 
                        else:
                            t += counter
                            counter =0 
            else:
                stk.append([s[i], 0])
        
        return t
            