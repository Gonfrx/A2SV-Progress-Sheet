class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        sum2 = sum1 = 0
        n = len(nums)
        l1 = 0 
        r1 = k - 1
        r2 = n - k
        l2 = n - 1 
        mx = 0 

        sum1 = sum(nums[:k])
        sum2 = sum(nums[-1:-k-1:-1])
        
        while(k > 0):
            if(sum1 >= sum2): 
                mx += nums[l1]
                sum1 -= nums[l1]
                sum2 -= nums[r2]
                r2 += 1
                l1 += 1
            else: 
                mx += nums[l2]
                sum2 -= nums[l2]
                sum1 -= nums[r1]
                r1 -= 1
                l2 -= 1
            k -= 1
        
        return mx