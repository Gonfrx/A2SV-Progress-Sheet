class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0 
        while n >= 2: 
            if n % 2 == 0: 
                n //= 2 
                count+=n
            else: 
                n //=2 
                count += n
                n +=1 
            print(n)
        return count