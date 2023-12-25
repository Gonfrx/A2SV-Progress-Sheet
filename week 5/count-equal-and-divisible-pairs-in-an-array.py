class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        #we cna brute force using 2 for loops 
        #for each value find all similar values and check if they satifsy
        #if they do increment the counter by 1
        counter = 0
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): 
                if nums[i] == nums[j]: 
                    if (i * j) % k == 0: 
                        counter+=1
        return counter
   
        