class Solution:
    def minimizedStringLength(self, s: str) -> int:
        count = 0
        st = set()
        for val in s: 
            if val not in st:  
                st.add(val) 
        return len(st)
        