class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pr = [0] * (len(nums)+1)

        for st, end in requests:
            pr[st] += 1
            pr[end+1] -= 1
    
        for i in range(1,len(pr)-1):
            pr[i] += pr[i-1]
        pr.pop()
        nums.sort()
        pr.sort()
        
        mx = 0
        for i in range(len(nums)):
            mx += nums[i] * pr[i]
        
        return (mx % (10 ** 9 + 7)) 

