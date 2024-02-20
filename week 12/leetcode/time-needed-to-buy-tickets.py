class Solution:
    def timeRequiredToBuy(self, nums: List[int], k: int) -> int:
        q = deque() 
        counter = 0

        for i in range(len(nums)):
            q.append([nums[i], i])
        while q: 
            t = q.popleft()
            t[0]-=1
            counter += 1
            if t[0] == 0: 
                if t[1] == k: 
                    return counter
            else:
                q.append(t) 
        
        return counter
            
        