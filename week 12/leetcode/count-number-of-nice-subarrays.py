class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #change the array to a binary arr
        arr  = []
        for val in nums:
            if val % 2 == 0: arr.append(0)
            else: arr.append(1)
        
        prefix = [0]
        for i in range(len(arr)): prefix.append(prefix[-1]+arr[i])

        ans = []
        counter = l = 0
        for i in range(len(prefix)):
            curr = 0

            if prefix[i] == prefix[i-1]:
                if prefix[i] >= k:
                    ans.append(ans[-1]) 
                    continue
            while prefix[i] - prefix[l] >= k: 
                if prefix[i] - prefix[l] == k:
                    curr += 1
                l += 1
            ans.append(curr) 

        return sum(ans) 