class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        start = []
        mx  = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i]-1 not in s: 
                start.append(nums[i])
        for val in start: 
            curr = 0
            v = val 
            while(v in s):
                v+=1
                curr += 1
            mx = max(curr, mx)
        return mx

        
        