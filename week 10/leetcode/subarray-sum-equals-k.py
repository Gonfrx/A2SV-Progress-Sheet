class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        counter = curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if (curr - k) in dic:
                counter += dic[curr-k]
            dic[curr] += 1

        return counter 
