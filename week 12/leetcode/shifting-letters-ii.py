class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)-1
        prefix = [0] * (n + 1) 
        for shift in shifts:
            if shift[2] == 0:
                prefix[shift[0]] -= 1
                if shift[1] < n:   
                    prefix[shift[1] + 1] += 1
            else:
                prefix[shift[0]] += 1
                if shift[1] < n: 
                    prefix[shift[1] + 1] -= 1
        
        print(prefix)
        prefix_sum = []
        prefix_sum.append(prefix[0])
        for i in range(1, len(prefix)):
            prefix_sum.append(prefix_sum[-1] + prefix[i])
        print(prefix_sum)
        ans = ""
#a - 1 = z 
        x = 0
       # print("ordz", ord('z'))
        for i in range(n+1):
        #print(ord(s[i]))
            x = ord(s[i]) - 97 
           # print(x)
            x += (prefix_sum[i] % 26)
            if x  < 0: 
                x += 26
            if x > 25:
                x -= 26
           # print(x)
            ans += chr(x + 97)
            
        return ans

        
        