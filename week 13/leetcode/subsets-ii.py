class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = tuple()
        ret = set()  

        def backtrack(idx): 
            nonlocal ans,ret
            ret.add(ans)

            for i in range(idx+1, len(nums)): 
                ans += (nums[i],)
                backtrack(i)
                ans = ans[:-1]
        
        backtrack(-1)
        ret = list({tuple(sorted(t)) for t in ret})
        
        return ret