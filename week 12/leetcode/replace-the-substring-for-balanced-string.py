class Solution:
    def balancedString(self, s: str) -> int:
        q = w = e = r = 0
        for i in range(len(s)):
            if s[i] == 'Q': q += 1
            elif s[i] == 'W': w += 1
            elif s[i] == 'E': e += 1
            else: r += 1
        
        ans = 0
        dic = defaultdict(int)
        dic2 = defaultdict(int)
        curr = l = 0
        mn = inf
        n = int(len(s) / 4)
        if q > n: dic['Q'] = q - n 
        if w > n: dic['W'] =  w - n
        if e > n: dic['E'] = e - n 
        if r > n: dic['R'] =  r - n
        if len(dic) == 0: 
            return 0

        
        for i in range(len(s)):
            dic2[s[i]] += 1
            curr += 1
            while l <= i and all(dic2.get(key, 0) >= count for key, count in dic.items()): 
                mn = min(mn, curr); 
                dic2[s[l]] -= 1
                if dic2[s[l]] == 0:
                    del dic2[s[l]]
                curr -= 1
                l += 1
            
        if mn == inf: 
            return 0
        return mn 
        # q q q w w w r r 
        