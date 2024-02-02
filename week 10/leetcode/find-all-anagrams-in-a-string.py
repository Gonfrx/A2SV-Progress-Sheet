class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        temp = 0 
        ans = []
        l = 0
        p_length = len(p)
        
        

        for i in range(p_length):
            dic1[p[i]] += 1
        for i in range(len(s)):
            dic2[s[i]] += 1
            temp += 1
            while temp >= p_length: 
                if dic1 == dic2:
                    ans.append(i - p_length +  1)
                if dic2[s[l]] > 1:
                    dic2[s[l]] -= 1
                else:
                    del dic2[s[l]]
                l+=1
                temp -= 1
            
        return ans 
        
        