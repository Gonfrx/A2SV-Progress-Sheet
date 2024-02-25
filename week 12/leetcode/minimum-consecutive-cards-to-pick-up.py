class Solution:
    def minimumCardPickup(self, nums: List[int]) -> int:
        l = curr = 0
        mn = inf
        dic = defaultdict(int)
        
        for i in range(len(nums)):
            dic[nums[i]] += 1
            curr += 1
            while dic[nums[i]] > 1:
                mn = min(mn, curr)
                if dic[nums[l]] > 1:
                    dic[nums[l]] -= 1
                else:
                    del dic[nums[l]]
                l += 1
                curr -= 1
             
        if mn == inf:
            return -1
        return mn