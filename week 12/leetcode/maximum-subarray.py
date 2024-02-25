class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        j = 0
        sum = nums[0]
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            sum = max(sum, curr)
            if curr < 0: curr = 0
        
        return sum

        