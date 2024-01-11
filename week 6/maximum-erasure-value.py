class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mx = 0
        curr = 0
        dic = defaultdict(int)
        l = 0
        dif = 0
        for i in range(len(nums)):
            dic[nums[i]]+=1

            while(dic[nums[i]] > 1):
                dif += nums[l]
                dic[nums[l]] -= 1
                l+=1

            curr += nums[i] 
            mx = max(mx, curr - dif)
            
        return mx 

        