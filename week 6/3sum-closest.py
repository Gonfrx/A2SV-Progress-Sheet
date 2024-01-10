class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = inf

        for i in range(len(nums)): 
            l = i + 1
            r = len(nums) - 1

            while(l < r):
                curr_sum = nums[i] + nums[l] + nums[r]
                if(abs(curr_sum - target) < abs(diff - target)):
                    diff = curr_sum
                if curr_sum == target: 
                    return curr_sum
                elif curr_sum > target:
                    r-=1
                else:
                    l+=1

        return diff
                







        