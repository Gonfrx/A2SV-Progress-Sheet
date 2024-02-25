class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = defaultdict(int)
        for char in s:
            mp[char] += 1
        
        count = 0
        flag = False
        for key, val in mp.items():
            if val %2 == 0: count+= val
            elif val == 1:
                if flag == False:
                    count += 1
                    flag = True
            else: 
                count += val - 1
        if flag == False:
            for key, val in mp.items():
                if val % 2 != 0: 
                    count += 1
                    break

    
        return count 