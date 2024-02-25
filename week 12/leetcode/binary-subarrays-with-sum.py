class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #there are 2 ways to approach this problem 
        #but both use similar methods 
        #one is using prefix sum array and if the current element is greater than the goal 
        #use left pointer until a subbary with lesser sum than the goal gets all this while having the sum
        #the second method is just to use pointers and ill try it now:

        count =  tot = sm = left = 0
        if goal == 0: 
            for i in range(len(nums)):
                if nums[i] == 1: 
                    count = 0
                else: count += 1
                tot += count
            return tot
        for i in range(len(nums)):
            if nums[i] == 1: 
                sm += 1
                count = 0
            while sm == goal: 
                count += 1
                if nums[left] == 1: sm-=1 
                left += 1
            tot += count
        
        return tot