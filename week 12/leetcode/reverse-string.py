class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0 
        r = len(s)-1
        def rev(s,l,r):
            if l >= r:
                return s
            s[l], s[r] = s[r], s[l]
            return rev(s,l+1,r-1)
        rev(s,l,r)
        