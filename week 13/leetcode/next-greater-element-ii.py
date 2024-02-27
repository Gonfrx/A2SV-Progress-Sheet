class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        
        stk = []
        ans = [0] * len(nums)
        for i in range(len(nums)):
            while stk and nums[i] > stk[-1][0]:
                ans[stk[-1][1]] = nums[i]
                stk.pop()
            stk.append([nums[i], i])
        
        n = len(stk)
        for i in range(n//2):
            stk.pop()
        while stk:
            ans[stk.pop()[1]] = -1
        
        a = []
        for i in range(len(ans)//2): 
            a.append(ans[i])
        
        return a
        

        