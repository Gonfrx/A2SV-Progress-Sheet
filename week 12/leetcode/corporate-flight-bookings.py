class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pf = [0] * (n+1)
        for start, end, cap in bookings:
            pf[start-1] += cap
            pf[end] -= cap
            
        for i in range(1, n+1):
            pf[i] += pf[i-1]
        
        return pf[:n]