class Solution:
    def minimumSteps(self, s: str) -> int:
        mn = 0
        one = 0 
        for i in range(len(s)):
            if s[i] == '0': 
                mn += one
            if s[i] == '1': one += 1
        return mn



        
       