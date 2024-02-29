class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ret = []
        def backtrack(idx):
            ret.append(ans.copy())  

            for i in range(idx+1, len(nums)): 
                ans.append(nums[i])
                backtrack(i)
                ans.pop()
        
        backtrack(-1)

        return ret 