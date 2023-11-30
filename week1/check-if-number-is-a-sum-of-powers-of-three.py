class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x = 0
        counter = 0  
        while x < n: 
            x = 3 ** counter
            counter+=1
        if x == n:
            return True
        counter-=2
        f = 3 ** counter
        while counter > 0:
            counter-=1
            temp = f + (3 ** counter)
            if temp < n:
                f = temp
            elif temp == n:
                return True
        return False