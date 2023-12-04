class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       main = ""
       l = 0
       r = 0
       while l < len(word1) and r < len(word2):
           temp = main + word1[l] + word2[r]
           main = temp
           l+=1 
           r+=1
       while l < len(word1):
           temp = main + word1[l]
           main = temp
           l += 1
       while r < len(word2):
           temp = main + word2[r]
           main = temp
           r +=1 
       return main 