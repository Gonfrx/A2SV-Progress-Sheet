class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        l = curr = mx = 0

        for i in range(len(s)):
            dic[s[i]] += 1
            curr += 1
            while dic[s[i]] > 1:
                if dic[s[l]] > 1:
                    dic[s[l]] -= 1
                else:
                    del dic[s[l]]
                l += 1
                curr -= 1
            mx = max(mx, curr)    

        return mx 