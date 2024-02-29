class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        ret = []

        def backtrack(idx):

            if idx >= len(nums): 
                ret.append(ans.copy())
                return 
            
            for i in range(len(nums)):
               if nums[i] not in ans:  
                    ans.append(nums[i])
                    backtrack(idx + 1)
                    ans.pop() 
        
        backtrack(0)
        return ret
        