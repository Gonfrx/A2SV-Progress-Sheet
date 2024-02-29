class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        ret = []
        def backtrack(idx):
            if sum(ans) == target: 
                ret.append(ans.copy())
                return 
            if sum(ans) > target:
                return 
            for i in range(len(nums)): 
                ans.append(nums[i])
                backtrack(idx +1)
                ans.pop()
        
        backtrack(0)
        unique_tuples = set(tuple(lst) for lst in ret)

        ret = list({tuple(sorted(t)) for t in unique_tuples})
        return ret 