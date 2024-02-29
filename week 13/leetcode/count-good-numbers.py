class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 5
        if n % 2 == 0: 
            even = n // 2
            odd = n // 2
        else:
            even = (n+1) // 2
            odd = (n-1) // 2
      
        result = (pow(5, even, MOD) * pow(4, odd, MOD)) % MOD
        
        return result
