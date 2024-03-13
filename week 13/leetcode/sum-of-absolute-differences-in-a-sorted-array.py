class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l = 0
        r = sum(nums[1:])
        left = 0  
        right = len(nums) - 1

        ans = []
        for i in range(len(nums)-1): 
            left_sum = (left * nums[i]) - l 
            right_sum = r - (right * nums[i])
            ans.append(left_sum + right_sum)

            l += nums[i] 
            r -= nums[i+1]
            left += 1
            right -= 1
        
        ans.append((nums[-1] * left) - l)
        
        return ans
        