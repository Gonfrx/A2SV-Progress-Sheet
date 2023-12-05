class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter =0 
        temp = 0
        for val in nums:
           if val == 1:
               temp += 1
               counter = max(temp, counter)
           else:
                counter = max(temp, counter)
                temp = 0
        counter = max(temp, counter)
        return counter 