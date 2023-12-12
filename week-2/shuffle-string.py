class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = []
        for val in s:
            arr.append(val)   
        count = 0
        for val in indices:
            arr[val] = s[count]
            count +=1 
        ans = ""
        for val in arr:
            ans += val
        return ans 