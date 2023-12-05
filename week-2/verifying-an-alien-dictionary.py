class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words)==1:
             return True
        l = 0
        r = 1 
        i = 0
        j = 0
        d = {}
        counter = 0
        for i in range(len(order)):
            d[order[i]] =  i
        i = 0
        while r < len(words):
            while i < len(words[l]) and j < len(words[r]):
                if d[words[l][i]] > d[words[r][j]]:
                    return False
                elif d[words[l][i]] == d[words[r][j]]:
                    counter+=1
                else:
                    break
                i+=1
                j+=1
            if counter == len(words[r]):
                if counter != len(words[l]):
                    return False
            i = 0
            j = 0
            counter = 0
            l+=1
            r+=1
        return True
                 