class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        per = 0
        l = 0
        m = 1
        r = 2
        while r < len(nums):
            if nums[l] + nums[m] > nums[r]:
                per = max(per, nums[l] + nums[m] + nums[r])
            l += 1
            m += 1
            r += 1
        return per
                