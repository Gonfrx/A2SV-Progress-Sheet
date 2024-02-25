class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicts = defaultdict(int)
        dictt = defaultdict(int)

        for char in t:
            dictt[char] += 1
        left = 0
        minimum = len(s) + 1
        
        n = len(s)
        minstring = ""
        for right in range(n):
            dicts[s[right]] += 1
            
                
            while all(dicts.get(key, 0) >= count for key, count in dictt.items()):
                if minimum >= right - left + 1:
                    minstring = s[left:right+1]
                minimum = min(minimum,right - left + 1)
                
                dicts[s[left]] -= 1
                if dicts[s[left]] == 0:
                    del dicts[s[left]]     
                left += 1
       
        return minstring