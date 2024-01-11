class Solution:
    def maxConsecutiveAnswers(self, nums: str, k: int) -> int:
        mx = curr= l = count =0  
        curr = k
        for i in range(len(nums)):
            count += 1
            if nums[i] != 'T':
                k -= 1
            while(l < len(nums) and k == -1): 
                if nums[l] == 'F':
                    k+=1
                l += 1
                count -= 1
            mx = max(mx, count)
        
        count = l = 0 
        k = curr
        for i in range(len(nums)): 
            count += 1
            if nums[i] != 'F':
                k -= 1
            while(l < len(nums) and k == -1):
                if nums[l] == 'T':
                    k+=1
                l += 1
                count -= 1
            mx = max(mx, count)
        
        return mx
            