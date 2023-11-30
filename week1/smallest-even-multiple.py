class Solution(object):
    def smallestEvenMultiple(self, n):
      x = n
      while(x % n != 0 or x % 2 != 0):
          x = x + 1
      return x 