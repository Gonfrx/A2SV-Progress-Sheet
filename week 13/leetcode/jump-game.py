class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        r = 1
        c = 0
        v = 1
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        while l < len(nums)-1 and r < len(nums)-1:
            if nums[l] > nums[r] + v:
                r += 1
                c = l
                v += 1
            else:
                l = r + 1
                l, r = r, l
                c = l
                v = 1
    
            if nums[c] == 0:
                return False
            
        return True

        