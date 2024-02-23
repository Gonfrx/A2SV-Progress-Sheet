class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c = 1
        mx = l = 0
        curr = -1

        for i in range(len(nums)):
            curr += 1
            if nums[i] == 0:
                c -= 1
            while c < 0: 
                if nums[l] == 0: 
                    c += 1
                l += 1
                curr -= 1
            mx = max(mx, curr)

        return mx 

        