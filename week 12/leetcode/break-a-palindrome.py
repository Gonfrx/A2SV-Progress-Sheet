class Solution:
    def breakPalindrome(self,s: str) -> str:
        if len(s) == 1: return ""
        ans = ""
        flag = False
        i = 0
        while i < len(s):
            if s[i] == 'a': 
                ans += s[i]
            else: 
                ans += 'a'
                flag = True
                i += 1
                while i < len(s):
                    ans += s[i]
                    i += 1
            i += 1
        
        if flag == False:
            if len(s) == 1: 
                return ""
            else: 
               ans = ans[:len(ans)-1]
               ans += 'b'
        
        check = False
        l = 0
        r = len(ans)-1
        while l < r: 
            if ans[l] != ans[r]: 
                check = True
                break
            l += 1
            r -= 1
        
        if check == False:
            s = s[:len(s)-1]
            s += 'b'
            return s
        return ans