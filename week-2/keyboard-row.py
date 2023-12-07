class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dec1 = {}
        dec2 = {}
        dec3 = {}
        str1 = "qwertyuiop"
        str2 = "asdfghjkl"
        str3 = "zxcvbnm"
        flag1 = True  
        flag2 = True
        flag3 = True
        arr = []
        for val in str1:
            dec1[val] = 1
        for val in str2:
            dec2[val] = 1
        for val in str3:
            dec3[val] = 1
        for val in words:
            flag1 = True
            flag2 = True
            flag3 = True
            for i in val:
                if i.lower() not in dec1:
                    flag1 = False
                if i.lower() not in dec2:
                    flag2 = False
                if i.lower() not in dec3:
                    flag3 = False 
            if flag1 or flag2 or flag3:
                arr.append(val)
           
        return arr           
            
