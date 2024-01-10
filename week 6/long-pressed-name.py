class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0
        r = 0

        while(l < len(name) and r < len(typed)):
            count = 0
            count2 = 0
            c = name[l]
            if name[l] != typed[r]:
                return False
            while(l < len(name) and name[l] == c):
                l+=1
                count+=1
            while(r < len(typed) and typed[r] == c):
                count2 += 1
                r+=1
            if count > count2:
                return False
        if l < len(name):
            return False
        if r < len(typed): 
            return False
        return True
