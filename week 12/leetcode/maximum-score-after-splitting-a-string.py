class Solution:
    def maxScore(self, s: str) -> int:
        sm =  zero = one = 0
        for i in range(len(s)): 
            if s[i] == '1': one += 1

        for i in range(len(s)-1):
            if s[i] == '1': 
                one -= 1
            elif s[i] == '0': 
                zero += 1
            sm = max(sm,one + zero)
        
        return sm
        