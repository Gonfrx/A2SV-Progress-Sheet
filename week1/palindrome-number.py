class Solution:
    def isPalindrome(self, x: int) -> bool:
       if(x < 0):
            return False
       if(x < 10):
           return True
       arr = []
       temp = 0 
       while(x > 1):
          temp = x % 10
          x = int(x / 10)
          arr.append(temp)
       temp = x % 10
       arr.append(temp)
       l = 0
       r = len(arr)-1
       if(arr[len(arr)-1] == 0):
           r-=1
       while(l != r and r > l):
           if(arr[l] != arr[r]):
               return False
           l+=1
           r-=1
       return True