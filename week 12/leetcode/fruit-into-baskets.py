class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        k = 1
        mx = l = curr = 0
        dic = defaultdict(int)

        for i in range(len(nums)):
            dic[nums[i]] += 1
            curr += 1
            while len(dic) > 2:
                if dic[nums[l]] > 1: 
                    dic[nums[l]] -= 1
                else:
                    del dic[nums[l]]
                l += 1
                curr -= 1
            
            mx = max(mx, curr)

        return mx