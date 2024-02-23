class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        x = len(arr)
        ans = []
        
        for i in range(x):
            mx = max(arr[:x - i])
            curr_max = arr.index(mx) + 1
            arr[:curr_max] = reversed(arr[:curr_max])
            ans.append(curr_max)
            
            arr[:x - i] = reversed(arr[:x - i])
            ans.append(x - i)
        return ans