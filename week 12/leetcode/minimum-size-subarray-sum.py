class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = l = 0
        mn = inf

        for i in range(len(nums)):
            curr += nums[i]
            while( curr >= target): 
                mn = min(mn, i - l+1)
                curr -= nums[l]
                l += 1
        if mn == inf: return 0
        return mn

        