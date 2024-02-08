class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        prefix_sum.append(nums[0])
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] * nums[i])
        
        ans = [0] * len(nums)
        count = curr =1 
        j = len(nums) - 2
        for i in range(len(nums)-1, -1, -1):
            if j >= 0: 
                ans[i] = (curr * prefix_sum[j])
            else:
                ans[i] = curr
            curr *= nums[i] 
            j -= 1

        return ans
        
        