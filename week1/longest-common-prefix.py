class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = 0
        main = strs[0] 
        n = len(main)
        mn = n
    
        for i in range(len(strs)):
            k = len(strs[i])
            counter = 0
            for j in range(min(n,k)):
                if main[j] == strs[i][j]:
                    counter += 1
                else:  
                    break
            if counter < mn:
                mn = counter
        return main[:mn]