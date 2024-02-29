class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = 0
        sm = 0
        r = 0
        while(r < k):
            sm += nums[r]
            r+=1
        avg = sm / k
        l = 0
        while(r < len(nums)):
            sm -= nums[l]
            l+=1
            sm += nums[r]
            r+=1
            avg = max(avg, sm / k)
        return avg

        


        