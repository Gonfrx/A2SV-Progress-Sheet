class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mx = max(arr)
        nums = [0] * (mx+1)
        for val in arr:
            nums[val] += 1
        mx = 0
        x = 0
        for i in range(len(nums)):
            if nums[i] > mx:
                mx = nums[i]
                x = i 
        return x
        
        