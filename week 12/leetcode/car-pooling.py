class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mx = 0
        for i in range(len(trips)): mx = max(trips[i][2], mx) 
        pf = [0] * (mx+1)

        for people, start, end in trips:
            pf[start] += people
            pf[end] -= people 
        
        for i in range(1, len(pf)): pf[i] += pf[i-1]
        for val in pf: 
            if val > capacity: return False
        
        return True