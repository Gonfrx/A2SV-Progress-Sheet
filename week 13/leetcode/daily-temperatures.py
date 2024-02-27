class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        st = []
        mp = defaultdict(int)

        for i in range(len(nums)):
            while len(st) > 0 and nums[i] > nums[st[-1]]:
                mp[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        
        ans = []
        for i in range(len(nums)):
            ans.append(mp[i])
        
        return ans
            