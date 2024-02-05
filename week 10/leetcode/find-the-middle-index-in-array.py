class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        r = sum(nums)
        l = 0
        for i in range(n):
            l += nums[i]
            if r == l:
                return i
            r -= nums[i]
        return -1
