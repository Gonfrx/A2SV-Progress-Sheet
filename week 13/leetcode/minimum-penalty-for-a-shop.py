class Solution:
    def bestClosingTime(self, arr: str) -> int:
        nums = []
        #[1,1,0,1]
        for val in arr:
            if val == 'Y': nums.append(1)
            else: nums.append(-1)
        
        curr = mx = 0
        idx = 0
        for i in range(len(nums)): 
            curr += nums[i]
            if curr > mx: 
                mx = curr
                idx = i

        if idx == 0: 
            if nums[0] == -1: 
                return 0
        return idx + 1 
        