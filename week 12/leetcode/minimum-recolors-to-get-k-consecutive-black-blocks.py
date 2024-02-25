class Solution:
    def minimumRecolors(self, nums: str, k: int) -> int:
        l = curr = 0 
        ws = 0
        for i in range(k):
            if nums[i] == 'W': ws += 1
        mn = ws
        r = k - 1

        while r < len(nums)-1:
            if nums[l] == 'W': 
                ws -= 1
            l += 1
            r += 1
            if nums[r] == 'W':
                ws += 1
            mn = min(mn, ws)

        return mn   
            
        