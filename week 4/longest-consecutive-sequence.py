class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        curr =1
        for i in range(len(nums)-1): 
            if nums[i+1] == (nums[i]+1): 
                curr += 1
                mx = max(curr, mx)
            elif nums[i+1] == nums[i]:
                curr += 0
                mx = max(curr, mx)
            else: 
                mx = max(curr, mx)
                curr = 1
        if len(nums) == 1:
            return 1
        return mx


        
        