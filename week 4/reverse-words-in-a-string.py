class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(map(str, s.split()))
        st = ""
        for i in range(len(arr)-1, 0, -1):
                st += arr[i]
                st += " " 
        st += arr[0]
        return st